from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from .settings import MEDIA_URL, MEDIA_ROOT


urlpatterns = [
    path('feederadmin/', admin.site.urls),

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

    path('user/', include('user.urls'), name='user'),
    path('spotify/', include('spotify.urls'), name='spotify'),
    path('youtube/', include('youtube.urls'), name='youtube'),
    path('subscription/', include('subscription.urls'), name='subscription'),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)
