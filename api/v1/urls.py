from django.urls import path, include

urlpatterns = [
    path('petrol-spy/', include('api.v1.petrol_spy.urls')),
]
