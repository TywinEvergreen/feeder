from django.urls import path

from .views import SubscriptionListCreateAPIView, SubscriptionDestroyAPIView


urlpatterns = [
    path('', SubscriptionListCreateAPIView.as_view(), name='subscriptions'),
    path('<pk>', SubscriptionDestroyAPIView.as_view(), name='subscription')
]
