from rest_framework.generics import CreateAPIView

from .serializers import ArtistSubscriptionSerializer, ChannelSubscriptionSerializer


class ArtistSubscriptionCreateAPIView(CreateAPIView):
    """
    Создаёт подписку на исполнителя
    """
    serializer_class = ArtistSubscriptionSerializer


class ChannelSubscriptionCreateAPIView(CreateAPIView):
    """
    Создаёт подписку на канал
    """
    serializer_class = ChannelSubscriptionSerializer
