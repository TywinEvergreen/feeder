from __future__ import absolute_import, unicode_literals
from django.core.files.base import ContentFile
from django.contrib.contenttypes.models import ContentType
from urllib.parse import urlparse
import requests
import datetime

from dateutil.parser import parse

from feeder.settings import SPOTIFY
from feeder.celery import app
from feeder.utils import delete_related_files
from notification.models import Notification
from .models import Artist, Album


@app.task
def get_new_albums():
    '''
    Обновляет альбомы в базе данных на новейшие из Spotify
    '''
    for artist in Artist.objects.all():
        sp_albums = SPOTIFY.artist_albums(artist.spotify_id, limit=50,
                                          album_type='album,single')['items']
        # Узнаем самый новый альбом
        newest = min(sp_albums, key=lambda x: datetime.datetime.now().date() - parse(x['release_date']).date())

        if not hasattr(artist, 'album') or \
           artist.album.release_date < parse(newest['release_date']).date():

            if hasattr(artist, 'album'):
                delete_related_files(artist.album)
                artist.album.delete()

            new_album = Album.objects.create(name=newest['name'], spotify_id=newest['id'],
                                             type=newest['type'], artist=artist,
                                             release_date=parse(newest['release_date']))

            cover_url = newest['images'][0]['url']
            cover_file = ContentFile(requests.get(cover_url).content)
            new_album.cover.save(f'{newest["release_date"]}_{new_album.name}_cover.jpg', cover_file)

            Notification.objects.create(
                content_type=ContentType.objects.get_for_model(new_album),
                object_id=new_album.pk
            )
