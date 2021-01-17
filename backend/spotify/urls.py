from django.urls import path

from .views import ArtistCreateAPIView


urlpatterns = [
    path('artist', ArtistCreateAPIView.as_view(), name='artist')
]
