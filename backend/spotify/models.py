from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.contenttypes.fields import GenericRelation

from feeder.settings import AUTH_USER_MODEL, UPLOAD_DIRECTORIES
from notification.models import DefaultNotification
from subscription.models import DefaultSubscription


class Artist(models.Model):
    name = models.CharField(max_length=256)
    spotify_id = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return f'{self.name}, #{self.pk}'


class ArtistSubscription(DefaultSubscription):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    subscriber = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE,
                                   related_name='artist_subscriptions')

    def __str__(self):
        return f'Подписка {self.subscriber.email} на исполнителя {self.artist.name}'


class Album(models.Model):
    album_types = (
        ('album', 'album'),
        ('single', 'single')
    )
    name = models.CharField(max_length=256)
    spotify_id = models.CharField(max_length=256, unique=True)
    cover = models.ImageField(upload_to=UPLOAD_DIRECTORIES['ALBUM_COVERS'], blank=True, null=True)
    type = models.CharField(choices=album_types, max_length=6)
    # Обратите внимание, что с исполнителем может быть
    # связан только один альбом, т.е. самый новый
    artist = models.OneToOneField(Artist, on_delete=models.CASCADE)
    release_date = models.DateField()

    def __str__(self):
        return f'{self.name}, #{self.pk}'

    class Meta:
        ordering = ['-release_date']
        

class AlbumNotification(DefaultNotification):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return f'Оповещение о новом альбоме {self.album.name} от исполнителя {self.album.artist.name}'