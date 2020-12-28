import sys
import os

from django.core.files.storage import default_storage
from django.core.files.uploadedfile import InMemoryUploadedFile
from datetime import datetime
from io import BytesIO

from PIL import Image
from dateutil.parser import parse

from feeder.settings import SPOTIFY
from feeder.utils import delete_related_files
from user.tests import AuthorizedAPITestCase
from .tasks import get_new_albums
from .models import Artist, Album


class ArtistTest(AuthorizedAPITestCase):

    def create_image(self, name, x=50, y=50):
        img_output = BytesIO()
        image = Image.new('RGB', (x, y), color='white')
        image.save(img_output, format='JPEG', quality=100)
        img_file = InMemoryUploadedFile(img_output, 'ImageField', f'{name}.jpg', 'image/jpeg',
                                        sys.getsizeof(img_output), 'utf-8')
        return img_file

    def test_related_names(self):
        artist = self.create_artist()

        self.user.followed_artists.add(artist)
        self.assertEqual(artist.following_users.last(), self.user)

    def test_delete_related_files(self):
        album = self.create_album()

        album.cover = self.create_image('img1')
        album.save()
        self.assertTrue(default_storage.exists('testing/img1.jpg'))

        delete_related_files(album)
        self.assertFalse(default_storage.exists('testing/img1.jpg'))


class TestSpotify(AuthorizedAPITestCase):

    def test_connection(self):
        response = SPOTIFY.artist('3o2dn2O0FCVsWDFSh8qxgG')
        self.assertEqual(response['id'], '3o2dn2O0FCVsWDFSh8qxgG')


class TestTasks(AuthorizedAPITestCase):

    def tearDown(self):
        for album in Album.objects.all():
            delete_related_files(album)

    def test_get_new_albums(self):
        artist = self.create_artist(spotify_id='3o2dn2O0FCVsWDFSh8qxgG')

        get_new_albums()
        artist.refresh_from_db()
        self.assertTrue(hasattr(artist, 'album'))
        self.assertTrue(artist.album.cover)

        artist.album.release_date = parse('1/1/1500')
        artist.album.save()

        get_new_albums()
        artist.refresh_from_db()
        self.assertNotEqual(artist.album.release_date, parse('1/1/1500'))
