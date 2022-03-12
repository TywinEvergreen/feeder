from django.contrib import admin

from subscription.models import ChannelSubscription


@admin.register(ChannelSubscription)
class ChannelSubscriptionAdmin(admin.ModelAdmin):
    list_display = ["channel", "subscriber", "datetime_committed"]
    search_fields = ["channel__name", "subscriber__email"]
