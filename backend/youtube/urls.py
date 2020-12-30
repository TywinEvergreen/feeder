from django.urls import path

from .views import ChannelCreateAPIView


urlpatterns = [
    path('channel/', ChannelCreateAPIView.as_view(), name='channel')
]
