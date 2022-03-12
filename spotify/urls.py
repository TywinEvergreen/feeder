from rest_framework import routers

from spotify.views import ArtistViewSet, NewAlbumsViewSet

app_name = "spotify"

router = routers.DefaultRouter()
router.register("artist", ArtistViewSet, basename="artist")
router.register("album-notifications", NewAlbumsViewSet, basename="album-notifications")

urlpatterns = router.urls
