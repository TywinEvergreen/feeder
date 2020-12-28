from django.contrib import admin

from .models import Artist, Album


class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'spotify_id')


class AlbumAdmin(admin.ModelAdmin):
    list_diplay = ('name', 'spotify_id', 'artist')


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Album, AlbumAdmin)
