from django.urls import path

from .views import ArtistCreateAPIView, NewAlubmsListAPIView


urlpatterns = [
    path('artist', ArtistCreateAPIView.as_view(), name='artist'),
    path('new-albums', NewAlubmsListAPIView.as_view(), name='new-albums')
]
