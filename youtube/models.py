from django.db import models


class Channel(models.Model):
    name = models.CharField(max_length=256)
    youtube_id = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return f'{self.name}, #{self.pk}'


class Video(models.Model):
    name = models.CharField(max_length=256)
    youtube_id = models.CharField(max_length=256, unique=True)
    cover = models.ImageField(upload_to='video_covers', blank=True, null=True)
    channel = models.OneToOneField(Channel, on_delete=models.CASCADE)
    release_datetime = models.DateTimeField()

    def __str__(self):
        return f'{self.name}, #{self.pk}'

    class Meta:
        ordering = ['-release_datetime']