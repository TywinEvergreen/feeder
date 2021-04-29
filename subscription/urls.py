from django.urls import path

from .views import ArtistSubscriptionCreateAPIView, ChannelSubscriptionCreateAPIView, \
    ArtistSubscriptionDestroyAPIView, ChannelSubscriptionDestroyAPIView


urlpatterns = [
    path('artist', ArtistSubscriptionCreateAPIView.as_view(), name='subscribe-artist'),
    path('artist/<pk>', ArtistSubscriptionDestroyAPIView.as_view(), name='destroy-artist-subscription'),
    path('channel', ChannelSubscriptionCreateAPIView.as_view(), name='subscribe-channel'),
    path('channel/<pk>', ChannelSubscriptionDestroyAPIView.as_view(), name='destroy-channel-subscription'),
]
