from django.db.models import OuterRef
from django.db.models.query import QuerySet
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from youtube.serializers import ChannelSerializer, VideoNotificationSerializer
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
    serializer_class = VideoNotificationSerializer

    def get_queryset(self) -> QuerySet[VideoNotification]:
        user = self.request.user

        queryset = VideoNotification.objects.filter(received_by=user).exclude(discarded_by=user)

        return queryset
