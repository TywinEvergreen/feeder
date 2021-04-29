from django.urls import path

from .views import ChannelCreateAPIView, NewVideosListAPIView


urlpatterns = [
    path('channel', ChannelCreateAPIView.as_view(), name='channel'),
    path('new-videos', NewVideosListAPIView.as_view(), name='new-videos')
]
