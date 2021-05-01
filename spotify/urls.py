from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from spotify.views import ArtistViewSet, NewAlbumsViewSet


router = routers.DefaultRouter()

router.register('artist', ArtistViewSet, basename='artist')
router.register('new-albums', NewAlbumsViewSet, basename='new-albums')

urlpatterns = [
    url('', include(router.urls))
]
