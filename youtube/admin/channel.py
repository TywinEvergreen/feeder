from django.contrib import admin

from youtube.models import Channel


@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ["name", "youtube_id"]
    search_fields = ["name"]
