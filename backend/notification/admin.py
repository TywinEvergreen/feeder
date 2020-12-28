from django.contrib import admin

from .models import Notification


class NotificationAdmin(admin.ModelAdmin):
    list_display = ('content_type', 'object_id',
                    'content_object', 'creation_date_time')


admin.site.register(Notification, NotificationAdmin)
