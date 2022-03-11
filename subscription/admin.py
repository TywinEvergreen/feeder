from django.contrib import admin

from subscription.models import ArtistSubscription, ChannelSubscription


@admin.register(ArtistSubscription)
class ArtistSubscriptionAdmin(admin.ModelAdmin):
    list_display = ["artist", "subscriber", "datetime_committed"]
    search_fields = ["artist__name", "subscriber__email"]


@admin.register(ChannelSubscription)
class ChannelSubscriptionAdmin(admin.ModelAdmin):
    list_display = ["channel", "subscriber", "datetime_committed"]
    search_fields = ["channel__name", "subscriber__email"]
