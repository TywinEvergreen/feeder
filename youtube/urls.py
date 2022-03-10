from rest_framework import routers

from youtube.views import ChannelViewSet, VideoNotificationViewSet


app_name = 'youtube'

router = routers.DefaultRouter()

router.register('channel', ChannelViewSet, basename='channel')
router.register('video-notifications', VideoNotificationViewSet, basename='video-notifications')

urlpatterns = router.urls
