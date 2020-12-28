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
        user = self.request.user
        queryset = Notification.objects.annotate(Count('album'), Count('video'))
        notifs_of_albums = queryset.filter(album__count__gte=1)
        notifs_of_videos = queryset.filter(video__count__gte=1)

        notifs_of_albums_to_user = notifs_of_albums.filter(
            album__artist__following_users=user
        )
        notifs_of_videos_to_user = notifs_of_videos.filter(
            video__channel__following_users=user
        )

        all_notifs_to_user = notifs_of_albums_to_user | notifs_of_videos_to_user

        return all_notifs_to_user.order_by('-creation_date_time')
