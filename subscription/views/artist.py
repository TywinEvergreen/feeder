from django.db.models.query import QuerySet
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from subscription.serializers import ArtistSubscriptionSerializer
from subscription.models import ArtistSubscription


class ArtistSubscriptionViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    """
    Создает или удаляет подписку на исполнителя
    """

    serializer_class = ArtistSubscriptionSerializer

    def get_queryset(self) -> QuerySet[ArtistSubscription]:
        return self.request.user.artist_subscriptions
