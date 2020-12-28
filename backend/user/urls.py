from django.urls import path

from .views import UserRetrieveUpdateAPIView


urlpatterns = [
    path('<pk>', UserRetrieveUpdateAPIView.as_view(), name='user')
]
