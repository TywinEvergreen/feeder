from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from .settings import MEDIA_URL, MEDIA_ROOT


urlpatterns = [
    path('feederadmin/', admin.site.urls),

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

    path('user/', include('user.urls', namespace='user')),
    path('spotify/', include('spotify.urls', namespace='spotify')),
    path('youtube/', include('youtube.urls', namespace='youtube')),
    path('subscription/', include('subscription.urls', namespace='subscription')),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)
