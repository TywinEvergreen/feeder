from rest_framework import serializers

from user.models import User
from spotify.serializers import ArtistSerializer
from youtube.serializers import ChannelSerializer
from .models import ArtistSubscription, ChannelSubscription


class ArtistSubscriptionSerializer(serializers.ModelSerializer):
    """
    Сериализует подписки на исполнителей
    """

    subscriber = serializers.StringRelatedField()

    class Meta:
        model = ArtistSubscription
        fields = "__all__"

    def create(self, validated_data) -> ArtistSubscription:
        user = self.context.get("request").user
        subscription, _ = ArtistSubscription.objects.get_or_create(
            **validated_data, subscriber=user
        )
        return subscription

    def to_representation(self, instance):
        self.fields["artist"] = ArtistSerializer()
        return super().to_representation(instance)


class ChannelSubscriptionSerializer(serializers.ModelSerializer):
    """
    Сериализует подписки на каналы
    """

    subscriber = serializers.StringRelatedField()

    class Meta:
        model = ChannelSubscription
        fields = "__all__"

    #
    def create(self, validated_data) -> ChannelSubscription:
        user = self.context.get("request").user
        subscription, _ = ChannelSubscription.objects.get_or_create(
            **validated_data, subscriber=user
        )
        return subscription

    def to_representation(self, instance):
        self.fields["channel"] = ChannelSerializer()
        return super().to_representation(instance)
