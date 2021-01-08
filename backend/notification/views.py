from django.db.models import Count
from rest_framework.generics import ListAPIView

from spotify.models import Artist
from youtube.models import Channel
from subscription.models import Subscription
from .serializers import NotificationSerializer
from .models import Notification


class NotificationListAPIView(ListAPIView):
    """
    Возвращает оповещения пользователя
    """
    serializer_class = NotificationSerializer

    def get_queryset(self):
        user = self.request.user

        queryset = Notification.objects.annotate(Count('album'), Count('video'))
        notifs_of_albums = queryset.filter(album__count__gte=1)
        notifs_of_videos = queryset.filter(video__count__gte=1)

        # Вместо .get использован .filter().first(), чтобы не вызывалось исключение
        notifs_of_albums_to_user = notifs_of_albums.filter(
            album__artist__in=Artist.objects.filter(subscriptions__subscriber=user),
            # Не стоит забывать, что здесь сравниваются DateField и
            # DateTimeField, поэтому результаты могуть быть неточными
            album__release_date__gte=user.subscriptions.filter(
                artist__in=Artist.objects.filter(
                    subscriptions__subscriber=user
                )
            ).first().datetime_committed
        )
        notifs_of_videos_to_user = notifs_of_videos.filter(
            video__channel__in=Channel.objects.filter(subscriptions__subscriber=user),
            video__release_datetime__gt=user.subscriptions.filter(
                channel__in=Channel.objects.filter(
                    subscriptions__subscriber=user
                )
            ).first().datetime_committed
        )

        all_notifs_to_user = notifs_of_albums_to_user.union(notifs_of_videos_to_user)

        return all_notifs_to_user.order_by('-creation_date_time')
