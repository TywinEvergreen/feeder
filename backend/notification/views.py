from django.db.models import Count
from rest_framework.generics import ListAPIView

from .serializers import NotificationSerializer
from .models import Notification


class NotificationListAPIView(ListAPIView):
    """
    Возвращает оповещения пользователя
    """
    serializer_class = NotificationSerializer

    def get_queryset(self):

        return Notification.objects.all()

        # user = self.request.user
        # queryset = Notification.objects.annotate(Count('album'), Count('video'))
        # notifs_of_albums = queryset.filter(album__count__gte=1)
        # notifs_of_videos = queryset.filter(video__count__gte=1)

        # notifs_of_albums_to_user = Notification.objects.filter(
        #     album__artist
        # )

        # notifs_of_albums_to_user = notifs_of_albums.filter(
        #     album__artist=user.subscriptions.get(author_obj=album__artist).album_artist,
        #     # album__release_date__gt=user.subscriptions.get(author_object=album__artist).datetime_committed
        # )
        # notifs_of_videos_to_user = notifs_of_videos.filter(
        #     video__channel__in=user.subscriptions.all(),
        # )

        # all_notifs_to_user = notifs_of_albums_to_user | notifs_of_videos_to_user

        # return all_notifs_to_user.order_by('-creation_date_time')
