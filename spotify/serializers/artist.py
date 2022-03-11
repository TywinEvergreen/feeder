from rest_framework import serializers

from spotify.models import Artist


class ArtistSerializer(serializers.ModelSerializer):
    spotify_id = serializers.CharField()
    name = serializers.CharField(required=False)

    class Meta:
        model = Artist
        fields = "__all__"

    def create(self, validated_data) -> Artist:
        artist, _ = Artist.objects.get_or_create(
            spotify_id=validated_data.get("spotify_id"),
            defaults={"name": validated_data.get("name")},
        )
        return artist

