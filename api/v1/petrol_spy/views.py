from datetime import timedelta, datetime
from django.db import connection
from django.db.models import Count, Max, Q
from django.contrib.auth.models import User
from django.db.models.functions import Coalesce
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import LeaderboardUserSerializer
from apps.petrol_spy.models import Report
from .swagger_docs import petrol_swagger_docs


class LeaderboardAPIView(APIView):
    @petrol_swagger_docs()
    def get(self, request, *args, **kwargs):
        latest_report_date = Report.objects.aggregate(latest_date=Max('created_at'))['latest_date']

        if not latest_report_date:
            return Response({"users": []}, status=status.HTTP_404_NOT_FOUND)

        thirty_days_ago = latest_report_date - timedelta(days=30)

        top_users = (
            User.objects.filter(reports__created_at__gte=thirty_days_ago)
            .annotate(
                reports_count=Count('reports', filter=Q(reports__created_at__gte=thirty_days_ago)),
                display_name=Coalesce('oneid_profile__full_name', 'username')
            )
            .order_by('-reports_count')[:100]
            .select_related('oneid_profile')
        )

        serializer = LeaderboardUserSerializer(top_users, many=True)
        return Response(data={"users": serializer.data}, status=status.HTTP_200_OK)


class LeaderboardWithSqlAPIView(APIView):
    @petrol_swagger_docs()
    def get(self, request, *args, **kwargs):
        with connection.cursor() as cursor:
            cursor.execute("SELECT MAX(created_at) FROM petrol_spy_report")
            latest_report_date = cursor.fetchone()[0]

        if not latest_report_date:
            return Response({"users": []}, status=status.HTTP_404_NOT_FOUND)

        if isinstance(latest_report_date, str):
            latest_report_date = datetime.fromisoformat(latest_report_date)
        thirty_days_ago = latest_report_date - timedelta(days=30)

        query = """
            SELECT
                SUM(r.reports_count) AS reports_count,
                r.user_id AS id,
                COALESCE(p.full_name, u.username) AS display_name
            FROM
                (SELECT
                    user_id,
                    COUNT(id) AS reports_count
                 FROM
                    petrol_spy_report
                 WHERE
                    created_at > %s
                 GROUP BY
                    user_id
                ) AS r
            LEFT JOIN
                users_oneidprofile p ON p.user_id = r.user_id
            JOIN
                auth_user u ON u.id = r.user_id
            GROUP BY
                r.user_id, p.full_name, u.username
            ORDER BY
                reports_count DESC
            LIMIT 100;
        """

        with connection.cursor() as cursor:
            cursor.execute(query, [thirty_days_ago])
            columns = [col[0] for col in cursor.description]
            results = [
                dict(zip(columns, row)) for row in cursor.fetchall()
            ]

        return Response(data={"users": results}, status=status.HTTP_200_OK)
