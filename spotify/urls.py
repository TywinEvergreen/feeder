from django.urls import path
from rest_framework import routers

from spotify.views import ArtistViewSet, NewAlbumsViewSet, ConnectSpotifyAccountApiView

app_name = "spotify"

router = routers.DefaultRouter()
router.register("artist", ArtistViewSet, basename="artist")
router.register("album-notifications", NewAlbumsViewSet, basename="album-notifications")

urlpatterns = [
    path("connect/", ConnectSpotifyAccountApiView.as_view(), name="connect"),
] + router.urls
