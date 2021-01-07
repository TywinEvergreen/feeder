from django.db.models import Count
from rest_framework.generics import ListAPIView

from spotify.models import Artist
from youtube.models import Channel
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

        subscribed_aritsts = Artist.objects.filter(subscriptions__subscriber=user)
        subscribed_channels = Artist.objects.filter(subscriptions__subscriber=user)
        print(subscribed_aritsts)
        print(subscribed_channels)

        notifs_of_albums_to_user = notifs_of_albums.filter(
            album__artist__in=Artist.objects.filter(subscriptions__subscriber=user),
            # album__release_date__gt=user.subscriptions.get(author_object=album__artist).datetime_committed
        )
        print(notifs_of_albums_to_user)
        notifs_of_videos_to_user = notifs_of_videos.filter(
            video__channel__in=Channel.objects.filter(subscriptions__subscriber=user),
        )
        print(notifs_of_videos_to_user)

        all_notifs_to_user = notifs_of_albums_to_user | notifs_of_videos_to_user

        return all_notifs_to_user.order_by('-creation_date_time')
