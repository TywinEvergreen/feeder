from django.urls import path

from .views import AlbumNotificationListAPIView, VideoNotificationListAPIView


urlpatterns = [
    path('album', AlbumNotificationListAPIView.as_view(), name='album-notifications'),
    path('video', VideoNotificationListAPIView.as_view(), name='video-notifications')
]
