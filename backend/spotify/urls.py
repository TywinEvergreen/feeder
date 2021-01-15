from django.urls import path

from .views import ArtistCreateAPIView, ArtistSubscriptionCreateAPIView, \
    AlbumNotificationListAPIView


urlpatterns = [
    path('artist', ArtistCreateAPIView.as_view(), name='artist'),
    path('subscribe', ArtistSubscriptionCreateAPIView.as_view(), name='artist-subscriptions'),
    path('notifications', AlbumNotificationListAPIView.as_view(), name='album-notifications')
]
