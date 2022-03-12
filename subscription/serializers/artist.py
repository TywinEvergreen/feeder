from rest_framework import serializers

from spotify.serializers import ArtistSerializer
from subscription.models import ArtistSubscription


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
