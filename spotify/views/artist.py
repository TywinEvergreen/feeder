from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from spotify.serializers import ArtistSerializer
from spotify.models import Artist


class ArtistViewSet(mixins.CreateModelMixin, GenericViewSet):
    """
    Создаёт исполнителя
    """

    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
