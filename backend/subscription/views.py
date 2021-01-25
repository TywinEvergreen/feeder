from django.db.models.query import QuerySet

from rest_framework.generics import CreateAPIView, DestroyAPIView

from .serializers import ArtistSubscriptionSerializer, ChannelSubscriptionSerializer
from .models import ArtistSubscription, ChannelSubscription


class ArtistSubscriptionCreateAPIView(CreateAPIView):
    """
    Создаёт подписку на исполнителя
    """
    serializer_class = ArtistSubscriptionSerializer


class ArtistSubscriptionDestroyAPIView(DestroyAPIView):
    """
    Удаляет подписку на исполнителя
    """

    def get_queryset(self) -> QuerySet[ArtistSubscription]:
        return self.request.user.artist_subscriptions


class ChannelSubscriptionCreateAPIView(CreateAPIView):
    """
    Создаёт подписку на канал
    """
    serializer_class = ChannelSubscriptionSerializer


class ChannelSubscriptionDestroyAPIView(DestroyAPIView):
    """
    Удаляет подписку на канал
    """

    def get_queryset(self) -> QuerySet[ChannelSubscription]:
        return self.request.user.channel_subscriptions