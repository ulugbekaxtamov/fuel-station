from django.urls import path
from .views import LeaderboardAPIView, LeaderboardWithSqlAPIView

app_name = 'api_user'

urlpatterns = [
    path('leaderboard/', LeaderboardAPIView.as_view(), name='leaderboard'),

    path('leaderboard/with-sql/', LeaderboardWithSqlAPIView.as_view(), name='leaderboard-sql'),
]
