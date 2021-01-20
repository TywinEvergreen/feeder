from django.db import models

from spotify.models import Album
from youtube.models import Video


# class DefaultNotification(models.Model):
#     creation_datetime = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         abstract = True
#         ordering = ['-creation_datetime']
#
#
# class AlbumNotification(DefaultNotification):
#     album = models.ForeignKey(Album, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f'Оповещение о новом альбоме {self.album.name} от исполнителя {self.album.artist.name}'
#
#
# class VideoNotification(DefaultNotification):
#     video = models.ForeignKey(Video, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f'Оповещение о новом видео {self.video.name} на канале {self.video.channel.name}'