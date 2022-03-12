from django.contrib import admin

from subscription.models import ArtistSubscription


@admin.register(ArtistSubscription)
class ArtistSubscriptionAdmin(admin.ModelAdmin):
    list_display = ["artist", "subscriber", "datetime_committed"]
    search_fields = ["artist__name", "subscriber__email"]
