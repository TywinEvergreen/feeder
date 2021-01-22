import sys
import os
from io import BytesIO

from django.core.files.storage import default_storage
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.urls import reverse

from PIL import Image
import pytz
from dateutil.parser import parse

from user.tests import AuthorizedAPITestCase
from .models import Artist, Album
from .tasks import get_new_albums


class TestArtist(AuthorizedAPITestCase):

    def create_image(self, name, x=50, y=50):
        img_output = BytesIO()
        image = Image.new('RGB', (x, y), color='white')
        image.save(img_output, format='JPEG', quality=100)
        img_file = InMemoryUploadedFile(img_output, 'ImageField', f'{name}.jpg', 'image/jpeg',
                                        sys.getsizeof(img_output), 'utf-8')
        return img_file

    def test_create_artist(self):
        response = self.client.post(reverse('artist'), {
            'spotify_id': '123',
            'name': 'test'
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['spotify_id'], '123')
        self.assertEqual(response.data['name'], 'test')

        response = self.client.post(reverse('artist'), {
            'spotify_id': '123'
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['spotify_id'], '123')
        self.assertEqual(response.data['name'], 'test')

    def test_delete_related_files(self):
        album = self.create_album()

        album.cover = self.create_image('img1')
        album.save()
        self.assertTrue(default_storage.exists('testing/img1.jpg'))

        album.delete()
        self.assertFalse(default_storage.exists('testing/img1.jpg'))

    def test_get_new_albums(self):
        artist = self.create_artist()
        self.create_artist_subscription(artist)
        album = self.create_album(artist)

        response = self.client.get(reverse('new-albums'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['count'], 1)


class TestTasks(AuthorizedAPITestCase):

    def test_get_new_albums(self):
        artist = self.create_artist(spotify_id='3o2dn2O0FCVsWDFSh8qxgG')

        get_new_albums()
        artist.refresh_from_db()
        self.assertTrue(hasattr(artist, 'album'))
        self.assertTrue(artist.album.cover)

        artist.album.release_datetime = pytz.utc.localize(parse('1/1/1500'))
        artist.album.save()

        get_new_albums()
        artist.refresh_from_db()
        self.assertNotEqual(artist.album.release_datetime, pytz.utc.localize(parse('1/1/1500')))