from django.db.models import OuterRef
from django.db.models.query import QuerySet
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from youtube.serializers import ChannelSerializer, VideoSerializer
from youtube.models import Channel, Video


class ChannelViewSet(mixins.CreateModelMixin, GenericViewSet):
    """
    Создаёт канал
    """
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer


class NewVideosViewSet(mixins.ListModelMixin, GenericViewSet):
    """
    Возвращает список видео с каналов, на которые подписан
    пользователь и которые вышли после подписки на канал
    """
    serializer_class = VideoSerializer

    def get_queryset(self) -> QuerySet[Video]:
        user = self.request.user
        queryset = Video.objects.filter(
            channel__in=user.channel_subscriptions.all().values('channel'),
            release_datetime__gte=user.channel_subscriptions.filter(
                channel=OuterRef('channel')
            ).values('datetime_committed')
        )
        return queryset
