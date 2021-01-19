from rest_framework import serializers

from user.models import User
from spotify.serializers import ArtistSerializer
from youtube.serializers import ChannelSerializer
from .models import ArtistSubscription, ChannelSubscription


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

    def to_representation(self, instance):
        self.fields['artist'] = ArtistSerializer()
        return super().to_representation(instance)


class ChannelSubscriptionSerializer(serializers.ModelSerializer):
    """
    Сериализует подписки на каналы
    """
    subscriber = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)

    class Meta:
        model = ChannelSubscription
        fields = '__all__'

    def create(self, validated_data):
        user = self.context.get('request').user
        subscription = ChannelSubscription.objects.create(**validated_data, subscriber=user)
        return subscription

    def to_representation(self, instance):
        self.fields['channel'] = ChannelSerializer()
        return super().to_representation(instance)