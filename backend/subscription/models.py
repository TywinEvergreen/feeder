from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from feeder.settings import AUTH_USER_MODEL


class Subscription(models.Model):
    author_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    author_id = models.PositiveIntegerField()
    author_object = GenericForeignKey('author_type', 'author_id')

    subscriber = models.ForeignKey(AUTH_USER_MODEL, related_name='subscriptions',
                                   on_delete=models.CASCADE)
    datetime_committed = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-datetime_committed']