from django.db.models import OuterRef

from rest_framework.generics import CreateAPIView, ListAPIView

from .serializers import ArtistSerializer, ArtistSubscriptionSerializer, \
    AlbumNotificationSerializer
from .models import AlbumNotification, Artist


class ArtistCreateAPIView(CreateAPIView):
    """
    Создаёт исполнителя
    """
    serializer_class = ArtistSerializer


class ArtistSubscriptionCreateAPIView(CreateAPIView):
    """
    Создаёт подписку на исполнителя
    """
    serializer_class = ArtistSubscriptionSerializer


class AlbumNotificationListAPIView(ListAPIView):
    """
    Возвращает лист оповещений об альбомах для пользователя
    """
    serializer_class = AlbumNotificationSerializer

    def get_queryset(self):
        user = self.request.user
        u = user.artist_subscriptions.filter(
            artist=OuterRef('sa')
        )
        queryset = AlbumNotification.objects.filter(
            album__artist__in=user.artist_subscriptions.all().values('artist'),
            album__release_date__gte=user.artist_subscriptions.filter(
                artist__album=OuterRef('album')
            ).values('datetime_committed')
        )
        return queryset




