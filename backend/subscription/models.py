from django.db import models

from feeder.settings import AUTH_USER_MODEL


class DefaultSubscription(models.Model):
    datetime_committed = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ['-datetime_committed']