import sys
import os
from io import BytesIO

from django.core.files.storage import default_storage
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.urls import reverse

from PIL import Image

from user.tests import AuthorizedAPITestCase
from feeder.utils import delete_related_files
from .models import Artist, Album


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

        delete_related_files(album)
        self.assertFalse(default_storage.exists('testing/img1.jpg'))