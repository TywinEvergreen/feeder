from django.db.models.query import QuerySet
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from user.serializers import UserSerializer
from user.models import User


class UserViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet,
):
    """
    Получает одного пользователя или обновляет его
    """
    serializer_class = UserSerializer

    def get_object(self) -> QuerySet[User]:
        return self.request.user
