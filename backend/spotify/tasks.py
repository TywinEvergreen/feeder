from __future__ import absolute_import, unicode_literals
from django.core.files.base import ContentFile
import requests
import datetime

from dateutil.parser import parse

from feeder.settings import SPOTIFY
from feeder.celery import app
from feeder.utils import delete_related_files
from .models import Artist, Album


@app.task
def get_new_albums():
    '''
    Обновляет альбомы в базе данных на новейшие из Spotify
    '''
    for artist in Artist.objects.all():
        latest_album = SPOTIFY.artist_albums(artist.spotify_id, limit=1,
                                             album_type='album')['items'][0]
        latest_single = SPOTIFY.artist_albums(artist.spotify_id, limit=1,
                                              album_type='single')['items'][0]

        # Узнаем самый новый релиз
        newest_releases = [latest_album, latest_single]
        newest = min(newest_releases, key=lambda x: datetime.datetime.now().date() - parse(x['release_date']).date())

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
