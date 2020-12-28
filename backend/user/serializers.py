from rest_framework import serializers

from spotify.models import Artist
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализует пользователей
    """
    artist = serializers.IntegerField(required=False)

    class Meta:
        model = User
        fields = '__all__'

    def update(self, instance, validated_data):
        allowed_arguements = ['artist']

        for item in validated_data.items():
            assert item[0] in allowed_arguements, f'Аргумент {item[0]} не разрешён'
            if item[0] == 'artist':
                artist = Artist.objects.get(pk=item[1])
                if instance.followed_artists.filter(pk=artist.pk):
                    instance.followed_artists.remove(artist)
                else:
                    instance.followed_artists.add(artist)
            else:
                setattr(instance, item[0], item[1])

        instance.save()
        return instance
