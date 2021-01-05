from django.urls import path

from .views import SubscriptionListCreateAPIView


urlpatterns = [
    path('', SubscriptionListCreateAPIView.as_view(), name='subscriptions')
]
