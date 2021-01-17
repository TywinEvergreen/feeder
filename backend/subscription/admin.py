from django.contrib import admin

from .models import ArtistSubscription, ChannelSubscription


class ArtistSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('artist', 'subscriber')


class ChannelSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('channel', 'subscriber')


admin.site.register(ArtistSubscription, ArtistSubscriptionAdmin)
admin.site.register(ChannelSubscription, ChannelSubscriptionAdmin)