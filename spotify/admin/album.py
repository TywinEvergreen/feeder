from django.contrib import admin

from spotify.models import Album, AlbumNotification

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ["name", "spotify_id", "artist", "release_datetime"]
    readonly_fields = ["spotify_id", "artist", "release_datetime"]
    search_fields = ["name"]


@admin.register(AlbumNotification)
class AlbumNotificationAdmin(admin.ModelAdmin):
    list_display = ["album", "created_datetime"]
    search_fields = ["album__name"]
