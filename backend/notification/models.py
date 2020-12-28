from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Notification(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    creation_date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Оповещение о новом релизе {self.content_object.name}'

    class Meta:
        ordering = ['-creation_date_time']
