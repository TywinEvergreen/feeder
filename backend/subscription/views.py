from rest_framework.generics import ListCreateAPIView

from .models import Subscription
from .serializers import SubscriptionSerializer


class SubscriptionListCreateAPIView(ListCreateAPIView):
    """
    Получает подписки пользователя или создает подписку
    """
    serializer_class = SubscriptionSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Subscription.objects.filter(subscriber=user)
        return queryset

