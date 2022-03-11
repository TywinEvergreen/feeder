from django.contrib import admin

from youtube.models import Channel, Video, VideoNotification


class ChannelAdmin(admin.ModelAdmin):
    list_display = ["name", "youtube_id"]
    search_fields = ["name"]


class VideoAdmin(admin.ModelAdmin):
    list_display = ["name", "youtube_id", "channel", "release_datetime"]
    readonly_fields = ["youtube_id", "channel", "release_datetime"]
    search_fields = ["name"]


class VideoNotificationAdmin(admin.ModelAdmin):
    list_display = ["video", "created_datetime"]
    search_fields = ["video__name"]


admin.site.register(Channel, ChannelAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(VideoNotification, VideoNotificationAdmin)
