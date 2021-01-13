from django.db import models


class DefaultNotification(models.Model):
    creation_datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ['-creation_datetime']
