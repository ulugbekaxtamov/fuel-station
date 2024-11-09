from rest_framework import serializers


class LeaderboardUserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    display_name = serializers.CharField()
    reports_count = serializers.IntegerField()


class LeaderboardResponseSerializer(serializers.Serializer):
    users = LeaderboardUserSerializer(many=True)


class ErrorResponseSerializer(serializers.Serializer):
    detail = serializers.CharField()
