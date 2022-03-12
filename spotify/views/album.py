from django.db.models.query import QuerySet
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from spotify.serializers import AlbumNotificationSerializer
from spotify.models import AlbumNotification


class NewAlbumsViewSet(mixins.ListModelMixin, GenericViewSet):
    """
    Возвращает оповещения о новых альбомах
    """

    serializer_class = AlbumNotificationSerializer

    def get_queryset(self) -> QuerySet[AlbumNotification]:
        user = self.request.user
        queryset = AlbumNotification.objects.filter(received_by=user).exclude(
            discarded_by=user
        )
        return queryset
