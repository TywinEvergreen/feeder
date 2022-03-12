from django.contrib import admin

from spotify.models import Artist


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ["name", "spotify_id"]
    search_fields = ["name"]
