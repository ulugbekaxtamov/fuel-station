from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .serializers import LeaderboardResponseSerializer, ErrorResponseSerializer


def petrol_swagger_docs():
    return swagger_auto_schema(
        responses={
            200: LeaderboardResponseSerializer,
            404: ErrorResponseSerializer,
            500: ErrorResponseSerializer,
        }
    )
