from django.contrib import admin

from .models import Subscription


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('content_type', 'object_id', 'author',
                    'subscriber', 'datetime_committed')


admin.site.register(Subscription, SubscriptionAdmin)
