from django.urls import path

from .views import ChannelCreateAPIView, ChannelSubscriptionCreateAPIView, \
    VideoNotificationListAPIView


urlpatterns = [
    path('channel', ChannelCreateAPIView.as_view(), name='channel'),
    path('subscribe', ChannelSubscriptionCreateAPIView.as_view(), name='channel-subscriptions'),
    path('notifications', VideoNotificationListAPIView.as_view(), name='video-notifications')
]
