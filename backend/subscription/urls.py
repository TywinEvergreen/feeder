from django.urls import path

from .views import ArtistSubscriptionCreateAPIView, ChannelSubscriptionCreateAPIView


urlpatterns = [
    path('artist', ArtistSubscriptionCreateAPIView.as_view(), name='subscribe-artist'),
    path('channel', ChannelSubscriptionCreateAPIView.as_view(), name='subscribe-channel'),
]
