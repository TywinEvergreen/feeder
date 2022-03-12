from django.urls import path

from user.views import UserRetrieveUpdateAPIView

app_name = "user"
#
# router = routers.DefaultRouter()
#
# router.register('', UserRetrieveUpdateAPIView, basename='user')

urlpatterns = [path("", UserRetrieveUpdateAPIView.as_view(), name="detail")]
