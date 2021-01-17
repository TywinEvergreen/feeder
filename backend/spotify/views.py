from rest_framework.generics import CreateAPIView

from .serializers import ArtistSerializer


class ArtistCreateAPIView(CreateAPIView):
    """
    Создаёт исполнителя
    """
    serializer_class = ArtistSerializer




