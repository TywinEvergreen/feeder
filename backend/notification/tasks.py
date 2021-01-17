from __future__ import absolute_import, unicode_literals
from django.core.files.base import ContentFile
import requests
import datetime

from dateutil.parser import parse

from feeder.settings import SPOTIFY, YOUTUBE
from feeder.celery import app
from feeder.utils import delete_related_files
from spotify.models import Artist, Album
from youtube.models import Channel, Video
from .models import AlbumNotification, VideoNotification


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

            AlbumNotification.objects.create(album=new_album)


@app.task
def get_new_videos():
    """
    Обновляет youtube видео в базе данных на новейшие из Youtube API
    """
    for channel in Channel.objects.all():
        newest = YOUTUBE.search().list(
            channelId=channel.youtube_id, maxResults=1,
            part='snippet', order='date'
        ).execute()['items'][0]['snippet']

        if not hasattr(channel, 'video') or \
           channel.video.release_datetime < parse(newest['publishedAt']):

            if hasattr(channel, 'video'):
                delete_related_files(channel.video)
                channel.video.delete()

            new_video = Video.objects.create(
                name=newest['title'],
                youtube_id=newest['channelId'],
                channel=channel,
                release_datetime=parse(newest['publishedAt'])
            )

            cover_url = newest['thumbnails']['high']['url']
            cover_file = ContentFile(requests.get(cover_url).content)
            new_video.cover.save(f'{newest["publishedAt"]}_{new_video.name}_cover.jpg', cover_file)

            VideoNotification.objects.create(video=new_video)
