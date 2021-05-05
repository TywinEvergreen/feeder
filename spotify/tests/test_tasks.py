from django.test import TestCase
from dateutil.parser import parse
import pytz

from spotify.models import AlbumNotification
from spotify.tests.factories import ArtistFactory
from spotify.tasks import get_new_albums


class SpotifyTasksTest(TestCase):
    def setUp(self) -> None:
        self.artist = ArtistFactory(spotify_id='3o2dn2O0FCVsWDFSh8qxgG')

    def test_get_new_albums(self):
        self.artist.album.release_datetime = pytz.utc.localize(parse('1/1/1500'))
        self.artist.album.save()

        get_new_albums()
        self.artist.refresh_from_db()

        self.assertTrue(
            AlbumNotification.objects.filter(album=self.artist.album).exists()
        )
        self.assertNotEqual(
            self.artist.album.release_datetime,
            pytz.utc.localize(parse('1/1/1500'))
        )
