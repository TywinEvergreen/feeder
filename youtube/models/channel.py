from django.db import models


class Channel(models.Model):
    name = models.CharField(max_length=256)
    youtube_id = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return f"Channel, {self.name}, #{self.pk}"
