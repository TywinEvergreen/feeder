from rest_framework import serializers

from spotify.models import Artist, Album


class ArtistSerializer(serializers.ModelSerializer):
    """
    Сериализует исполнителей
    """
    spotify_id = serializers.CharField()
    name = serializers.CharField(required=False)

    class Meta:
        model = Artist
        fields = '__all__'

    def create(self, validated_data):
        artist, _ = Artist.objects.get_or_create(
            spotify_id=validated_data['spotify_id'],
            defaults={
                'name': validated_data.get('name')
            }
        )
        return artist

class AlbumSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer()

    class Meta:
        model = Album
        fields = '__all__'

