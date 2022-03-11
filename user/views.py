from django.db.models.query import QuerySet
from rest_framework import mixins, generics

from user.serializers import UserSerializer
from user.models import User


class UserRetrieveUpdateAPIView(generics.RetrieveAPIView, generics.UpdateAPIView):
    """
    Retrieves current user or updates them
    """

    serializer_class = UserSerializer

    def get_object(self) -> QuerySet[User]:
        return self.request.user
