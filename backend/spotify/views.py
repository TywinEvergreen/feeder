from django.db.models import OuterRef
from django.db.models.query import QuerySet

from rest_framework.generics import CreateAPIView, ListAPIView

from .serializers import ArtistSerializer, AlbumSerializer
from .models import Album


class ArtistCreateAPIView(CreateAPIView):
    """
    Создаёт исполнителя
    """
    serializer_class = ArtistSerializer


class NewAlubmsListAPIView(ListAPIView):
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


