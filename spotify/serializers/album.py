from rest_framework import serializers

from spotify.models import Album, AlbumNotification
from spotify.serializers.artist import ArtistSerializer


class AlbumSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer()

    class Meta:
        model = Album
        fields = "__all__"


class AlbumNotificationSerializer(serializers.ModelSerializer):
    album = AlbumSerializer()

    class Meta:
        model = AlbumNotification
        fields = "__all__"
