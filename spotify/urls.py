from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from spotify.views import ArtistViewSet, NewAlbumsViewSet


app_name = 'spotify'

router = routers.DefaultRouter()

router.register('artist', ArtistViewSet, basename='artist')
router.register('album-notifications', NewAlbumsViewSet, basename='album-notifications')

urlpatterns = [
    url('', include(router.urls))
]
