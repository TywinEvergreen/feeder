from rest_framework import serializers

from .models import User
from subscription.serializers import (
    ArtistSubscriptionSerializer,
    ChannelSubscriptionSerializer,
)


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализует пользователей
    """

    artist_subscriptions = ArtistSubscriptionSerializer(many=True)
    channel_subscriptions = ChannelSubscriptionSerializer(many=True)

    class Meta:
        model = User
        fields = "__all__"
