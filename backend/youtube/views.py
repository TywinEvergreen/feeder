from django.db.models import OuterRef
from rest_framework.generics import CreateAPIView, ListAPIView

from .serializers import ChannelSerializer, VideoSerializer
from .models import Video


class ChannelCreateAPIView(CreateAPIView):
    """
    Создаёт канал
    """
    serializer_class = ChannelSerializer


class NewVideosListAPIView(ListAPIView):
    """
    Возвращает список видео с каналов, на которые подписан
    пользователь и которые вышли после подписки на канал
    """
    serializer_class = VideoSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Video.objects.filter(
            channel__in=user.channel_subscriptions.all().values('channel'),
            release_datetime__gte=user.channel_subscriptions.filter(
                channel=OuterRef('channel')
            ).values('datetime_committed')
        )
        return queryset