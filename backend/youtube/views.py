from rest_framework.generics import CreateAPIView

from .serializers import ChannelSerializer


class ChannelCreateAPIView(CreateAPIView):
    """
    Создаёт канал
    """
    serializer_class = ChannelSerializer
