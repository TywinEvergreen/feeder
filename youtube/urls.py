from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from youtube.views import ChannelViewSet, NewVideosViewSet


app_name = 'youtube'

router = routers.DefaultRouter()

router.register('channel', ChannelViewSet, basename='channel')
router.register('new-videos', NewVideosViewSet, basename='new-videos')

urlpatterns = [
    url('', include(router.urls))
]
