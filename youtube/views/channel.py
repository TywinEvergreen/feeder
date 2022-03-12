from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from youtube.serializers import ChannelSerializer
from youtube.models import Channel


class ChannelViewSet(mixins.CreateModelMixin, GenericViewSet):
    """
    Создаёт канал
    """

    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer
