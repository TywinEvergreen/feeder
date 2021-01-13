from rest_framework import serializers

from user.models import User
from .models import Artist, ArtistSubscription, Album, AlbumNotification


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
            spotify_id=validated_data.get('spotify_id'),
            defaults={
                'name': validated_data.get('name')
            }
        )
        return artist


class ArtistSubscriptionSerializer(serializers.ModelSerializer):
    """
    Сериализует подписки на исполнителей
    """
    subscriber = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)

    class Meta:
        model = ArtistSubscription
        fields = '__all__'

    def create(self, validated_data):
        user = self.context.get('request').user
        subscription = ArtistSubscription.objects.create(**validated_data, subscriber=user)
        return subscription


class AlbumNotificationSerializer(serializers.ModelSerializer):
    """
    Сериализует оповещения об альбомах
    """

    class Meta:
        model = AlbumNotification
        fields = '__all__'
