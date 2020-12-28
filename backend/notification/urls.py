from django.urls import path, include

from .views import NotificationListAPIView


urlpatterns = [
    path('', NotificationListAPIView.as_view(), name='notifications'),
]
