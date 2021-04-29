from rest_framework.generics import UpdateAPIView

from .serializers import UserSerializer
from .models import User


class UserUpdateAPIView(UpdateAPIView):
    """
    Получает одного пользователя или обновляет его
    """
    serializer_class = UserSerializer

    def get_object(self) -> 'User':
        return self.request.user
