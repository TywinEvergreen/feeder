from rest_framework import serializers

from youtube.serializers import ChannelSerializer
from subscription.models import ChannelSubscription


class ChannelSubscriptionSerializer(serializers.ModelSerializer):
    """
    Сериализует подписки на каналы
    """

    subscriber = serializers.StringRelatedField()

    class Meta:
        model = ChannelSubscription
        fields = "__all__"

    def create(self, validated_data) -> ChannelSubscription:
        user = self.context.get("request").user
        subscription, _ = ChannelSubscription.objects.get_or_create(
            **validated_data, subscriber=user
        )
        return subscription

    def to_representation(self, instance):
        self.fields["channel"] = ChannelSerializer()
        return super().to_representation(instance)
