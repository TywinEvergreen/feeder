from django.db.models import OuterRef
from django.db.models.query import QuerySet
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from spotify.serializers import ArtistSerializer, AlbumSerializer
from spotify.models import Album, Artist


class ArtistViewSet(mixins.CreateModelMixin, GenericViewSet):
    """
    Создаёт исполнителя
    """
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class NewAlbumsViewSet(mixins.ListModelMixin, GenericViewSet):
    """
    Возвращает список альбомов, на исполнителей которых подписан
    пользователь и которые вышли после подписки на исполнителя
    """
    serializer_class = AlbumSerializer

    def get_queryset(self) -> QuerySet[Album]:
        user = self.request.user
        queryset = Album.objects.filter(
            artist__in=user.artist_subscriptions.all().values('artist'),
            # Результаты могут быть неточными, т.к.
            # сравниваются DateField и DateTimeField
            release_datetime__gte=user.artist_subscriptions.filter(
                artist=OuterRef('artist')
            ).values('datetime_committed')
        )
        return queryset


