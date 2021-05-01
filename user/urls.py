from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from user.views import UserViewSet


router = routers.DefaultRouter()

router.register('user', UserViewSet, basename='user')

urlpatterns = [
    url('', include(router.urls))
]
