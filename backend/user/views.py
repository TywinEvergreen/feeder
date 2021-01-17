from rest_framework.generics import UpdateAPIView

from .serializers import UserSerializer


class UserUpdateAPIView(UpdateAPIView):
    """
    Получает одного пользователя или обновляет его
    """
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
