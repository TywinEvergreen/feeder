from rest_framework.generics import RetrieveUpdateAPIView

from .models import User
from .serializers import UserSerializer
from .permissions import IsCurrentUserOrReadOnly


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    """
    Получает одного пользователя или обновляет его
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsCurrentUserOrReadOnly]
