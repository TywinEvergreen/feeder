from django.contrib import admin

from .models import AlbumNotification, VideoNotification


class AlbumNotificationAdmin(admin.ModelAdmin):
    list_display = ('album',)


class VideoNotificationAdmin(admin.ModelAdmin):
    list_display = ('video',)


admin.site.register(AlbumNotification, AlbumNotificationAdmin)
admin.site.register(VideoNotification, VideoNotificationAdmin)
