from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from user.views import UserRetrieveUpdateAPIView


app_name = 'user'

router = routers.DefaultRouter()

router.register('', UserRetrieveUpdateAPIView, basename='user')

urlpatterns = [
    url('', include(router.urls))
]
