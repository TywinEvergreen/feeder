from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.contenttypes.fields import GenericRelation

from feeder.settings import UPLOAD_DIRECTORIES
from notification.models import Notification


class Artist(models.Model):
    name = models.CharField(max_length=256)
    spotify_id = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return f'{self.name}, #{self.pk}'


class Album(models.Model):
    album_types = (
        ('album', 'album'),
        ('single', 'single')
    )
    name = models.CharField(max_length=256)
    spotify_id = models.CharField(max_length=256, unique=True)
    cover = models.ImageField(upload_to=UPLOAD_DIRECTORIES['ALBUM_COVERS'], blank=True, null=True)
    type = models.CharField(choices=album_types, max_length=6)
    artist = models.OneToOneField(Artist, on_delete=models.CASCADE)
    release_date = models.DateField()

    notification = GenericRelation(Notification, related_query_name='album')

    def __str__(self):
        return f'{self.name}, #{self.pk}'

    class Meta:
        ordering = ['-release_date']
