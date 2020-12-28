from django.contrib import admin

from .models import Channel, Video


class ChannelAdmin(admin.ModelAdmin):
    list_display = ('name', 'youtube_id')


class VideoAdmin(admin.ModelAdmin):
    list_diplay = ('name', 'youtube_id', 'youtuber')


admin.site.register(Channel, ChannelAdmin)
admin.site.register(Video, VideoAdmin)
