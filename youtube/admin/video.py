from django.contrib import admin

from youtube.models import Video, VideoNotification


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ["name", "youtube_id", "channel", "release_datetime"]
    readonly_fields = ["youtube_id", "channel", "release_datetime"]
    search_fields = ["name"]


@admin.register(VideoNotification)
class VideoNotificationAdmin(admin.ModelAdmin):
    list_display = ["video", "created_datetime"]
    search_fields = ["video__name"]
