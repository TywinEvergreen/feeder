from django.urls import path, include

urlpatterns = [
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
    path("user/", include("user.urls")),
    path("spotify/", include("spotify.urls")),
    path("youtube/", include("youtube.urls")),
    path("subscription/", include("subscription.urls")),
]
