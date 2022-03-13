from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from .settings import MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    path("adm1n/", admin.site.urls),
    path("api/", include("feeder.api_urls")),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)
