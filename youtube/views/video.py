from django.db.models.query import QuerySet
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from youtube.serializers import VideoNotificationSerializer
from youtube.models import VideoNotification


class VideoNotificationViewSet(mixins.ListModelMixin, GenericViewSet):
    """
    Возвращает оповещения о новых видео
    """

    serializer_class = VideoNotificationSerializer

    def get_queryset(self) -> QuerySet[VideoNotification]:
        user = self.request.user
        queryset = VideoNotification.objects.filter(received_by=user).exclude(
            discarded_by=user
        )

        return queryset
