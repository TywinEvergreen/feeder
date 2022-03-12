from django.db import models


class DefaultSubscription(models.Model):
    datetime_committed = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ["-datetime_committed"]
