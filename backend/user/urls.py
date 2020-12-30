from django.urls import path

from .views import UserUpdateAPIView


urlpatterns = [
    path('', UserUpdateAPIView.as_view(), name='user')
]
