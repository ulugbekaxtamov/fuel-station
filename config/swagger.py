from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Leaderboards API",
        default_version='v1',
        description="Leaderboards API documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="info@example.icu"),
        license=openapi.License(name="Leaderboards API"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],

)
