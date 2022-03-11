from __future__ import absolute_import, unicode_literals
import requests
import datetime

from django.core.files.base import ContentFile

from dateutil.parser import parse
from pytz import utc

from feeder.settings import SPOTIFY
from feeder.celery import app
from spotify.models import Artist, Album, AlbumNotification


@app.task
def get_new_albums():
    """
    Обновляет альбомы в базе данных на новейшие из Spotify
    """
    for artist in Artist.objects.all():
        latest_album = SPOTIFY.artist_albums(
            artist.spotify_id, limit=1, album_type="album"
        )["items"]
        latest_single = SPOTIFY.artist_albums(
            artist.spotify_id, limit=1, album_type="single"
        )["items"]

        releases = latest_album + latest_single

        if releases:
            newest = min(
                releases,
                key=lambda x: datetime.datetime.now().date()
                - parse(x["release_date"]).date(),
            )

            if (
                not hasattr(artist, "album")
                or artist.album.release_datetime.date()
                < parse(newest["release_date"]).date()
            ):
                if hasattr(artist, "album"):
                    artist.album.delete()

                new_album = Album.objects.create(
                    name=newest["name"],
                    spotify_id=newest["id"],
                    type=newest["type"],
                    artist=artist,
                    release_datetime=utc.localize(parse(newest["release_date"])),
                )

                cover_url = newest["images"][0]["url"]
                cover_file = ContentFile(requests.get(cover_url).content)
                new_album.cover.save(
                    f'{newest["release_date"]}_{new_album.name}_cover.jpg', cover_file
                )
