from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from .settings import MEDIA_URL, MEDIA_ROOT


urlpatterns = [
    path('admin-panel/', admin.site.urls),

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

    path('user/', include('user.urls')),
    path('spotify/', include('spotify.urls')),
    path('youtube/', include('youtube.urls')),
    path('subscriptions/', include('subscription.urls'))
] + static(MEDIA_URL, document_root=MEDIA_ROOT)
