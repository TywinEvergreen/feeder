from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

from feeder.settings import AUTH_USER_MODEL, UPLOAD_DIRECTORIES
from notification.models import DefaultNotification
from subscription.models import DefaultSubscription


class Channel(models.Model):
    name = models.CharField(max_length=256)
    youtube_id = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return f'{self.name}, #{self.pk}'

class ChannelSubscription(DefaultSubscription):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    subscriber = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE,
                                   related_name='channel_subscriptions')

    def __str__(self):
        return f'Подписка {self.subscriber.email} на канал {self.channel.name}'


class Video(models.Model):
    name = models.CharField(max_length=256)
    youtube_id = models.CharField(max_length=256, unique=True)
    cover = models.ImageField(upload_to=UPLOAD_DIRECTORIES['VIDEO_COVERS'], blank=True, null=True)
    channel = models.OneToOneField(Channel, on_delete=models.CASCADE)
    release_datetime = models.DateTimeField()

    def __str__(self):
        return f'{self.name}, #{self.pk}'

    class Meta:
        ordering = ['-release_datetime']


class VideoNotification(DefaultNotification):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)

    def __str__(self):
        return f'Оповещение о новом видео {self.video.name} на канале {self.video.channel.name}'