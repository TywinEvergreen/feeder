from django.urls import path

from .views import UserUpdateAPIView


urlpatterns = [
    path('', SubscriptionListCreateAPIView.as_view(), name='subscriptions')
]
