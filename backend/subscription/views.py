from rest_framework.generics import ListCreateAPIView, DestroyAPIView

from .permissions import OnlyCurrentUserSubscriptions
from .serializers import SubscriptionSerializer
from .models import Subscription


class SubscriptionListCreateAPIView(ListCreateAPIView):
    """
    Получает подписки пользователя или создает подписку
    """
    serializer_class = SubscriptionSerializer

    def get_queryset(self):
        return self.request.user.subscriptions.all()


class SubscriptionDestroyAPIView(DestroyAPIView):
    """
    Удаляет подписки пользователя
    """
    serializer_class = SubscriptionSerializer

    def get_queryset(self):
        return self.request.user.subscriptions.all()

