from django.db.models.query import QuerySet
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from subscription.serializers import ChannelSubscriptionSerializer
from subscription.models import ChannelSubscription


class ChannelSubscriptionViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    """
    Создает или удаляет подписку на канал
    """

    serializer_class = ChannelSubscriptionSerializer

    def get_queryset(self) -> QuerySet[ChannelSubscription]:
        return self.request.user.channel_subscriptions
