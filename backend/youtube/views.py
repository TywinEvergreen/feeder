from django.db.models import OuterRef

from rest_framework.generics import CreateAPIView, ListAPIView

from .serializers import ChannelSerializer, ChannelSubscriptionSerializer, \
    VideoNotificationSerializer
from .models import VideoNotification


class ChannelCreateAPIView(CreateAPIView):
    """
    Создаёт канал
    """
    serializer_class = ChannelSerializer


class ChannelSubscriptionCreateAPIView(CreateAPIView):
    """
    Создаёт подписку на канал
    """
    serializer_class = ChannelSubscriptionSerializer


class VideoNotificationListAPIView(ListAPIView):
    """
    Возвращает лист оповещений о видео для пользователя
    """
    serializer_class = VideoNotificationSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = VideoNotification.objects.filter(
            video__channel__in=user.channel_subscriptions.all().values('channel'),
            video__release_datetime__gte=user.channel_subscriptions.filter(
                channel__video=OuterRef('video')
            ).values('datetime_committed')
        )
        return queryset