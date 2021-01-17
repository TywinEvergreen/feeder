from django.urls import path

from .views import AlbumNotificationListAPIView, VideoNotificationListAPIView


urlpatterns = [
    path('albums', AlbumNotificationListAPIView.as_view(), name='album-notifications'),
    path('videos', VideoNotificationListAPIView.as_view(), name='video-notifications')
]
