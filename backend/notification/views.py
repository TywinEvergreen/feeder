from django.db.models import OuterRef

from rest_framework.generics import ListAPIView

from .serializers import AlbumNotificationSerializer, VideoNotificationSerializer
from .models import AlbumNotification, VideoNotification


class AlbumNotificationListAPIView(ListAPIView):
    """
    Возвращает лист оповещений об альбомах пользователю
    """
    serializer_class = AlbumNotificationSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = AlbumNotification.objects.filter(
            album__artist__in=user.artist_subscriptions.all().values('artist'),
            # Результаты могут быть неточными, т.к.
            # сравниваются DateField и DateTimeField
            album__release_date__gte=user.artist_subscriptions.filter(
                artist__album=OuterRef('album')
            ).values('datetime_committed')
        )
        return queryset


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