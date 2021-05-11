from django.db import models

from user.models import User


class Artist(models.Model):
    name = models.CharField(max_length=256)
    spotify_id = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return f'Artist, {self.name}, #{self.pk}'


class Album(models.Model):
    ALBUM = 'album'
    SINGLE = 'single'

    TYPE_CHOICES = (
        (ALBUM, 'Альбом'),
        (SINGLE, 'Сингл')
    )

    name = models.CharField(max_length=256)
    spotify_id = models.CharField(max_length=256, unique=True)
    cover = models.ImageField(upload_to='album_covers', blank=True, null=True)
    type = models.CharField(choices=TYPE_CHOICES, max_length=6)
    artist = models.OneToOneField(Artist, on_delete=models.CASCADE)

    release_datetime = models.DateTimeField()

    def __str__(self):
        return f'Album, {self.name}, #{self.pk}'

    class Meta:
        ordering = ['-release_datetime']


class AlbumNotification(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, verbose_name='Альбом')
    created_datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Оповещения об альбомах'
