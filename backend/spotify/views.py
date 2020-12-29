from rest_framework.generics import CreateAPIView

from .models import Artist
from .serializers import ArtistSerializer


class ArtistCreateAPIView(CreateAPIView):
    """
    Создаёт исполнителя
    """
    serializer_class = ArtistSerializer
