from django.db.models import OuterRef
from django.db.models.query import QuerySet
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from youtube.serializers import ChannelSerializer, VideoSerializer
from youtube.models import Channel, VideoNotification


class ChannelViewSet(mixins.CreateModelMixin, GenericViewSet):
    """
    Создаёт канал
    """
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer


class VideoNotificationViewSet(mixins.ListModelMixin, GenericViewSet):
    """
    Возвращает список видео с каналов, на которые подписан
    пользователь и которые вышли после подписки на канал
    """
    serializer_class = VideoSerializer

    # TODO: Переделать под VideoNotification
    def get_queryset(self) -> QuerySet[VideoNotification]:
        user = self.request.user
        subscribed_channels = user.channel_subscriptions.all().values('channel')
        queryset = VideoNotification.objects.filter(
            video__channel__in=subscribed_channels,
            release_datetime__gte=user.channel_subscriptions.filter(
                channel=OuterRef('video__channel')
            ).values('datetime_committed')
        )
        return queryset
