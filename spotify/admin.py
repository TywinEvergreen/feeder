from django.contrib import admin

from spotify.models import Artist, Album, AlbumNotification


class ArtistAdmin(admin.ModelAdmin):
    list_display = ["name", "spotify_id"]
    search_fields = ["name"]


class AlbumAdmin(admin.ModelAdmin):
    list_display = ["name", "spotify_id", "artist", "release_datetime"]
    readonly_fields = ["spotify_id", "artist", "release_datetime"]
    search_fields = ["name"]


class AlbumNotificationAdmin(admin.ModelAdmin):
    list_display = ["album", "created_datetime"]
    search_fields = ["album__name"]


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(AlbumNotification, AlbumNotificationAdmin)
