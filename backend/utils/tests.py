import sys
import os
from io import BytesIO

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.storage import default_storage

from PIL import Image

from user.tests import AuthorizedAPITestCase
from .tasks import cleanup_unused_files


class UtilsTest(AuthorizedAPITestCase):

    def create_image(self, name, x=1, y=1):
        img_output = BytesIO()
        image = Image.new('RGB', (x, y), color='white')
        image.save(img_output, format='JPEG', quality=100)
        img_file = InMemoryUploadedFile(img_output, 'ImageField', f'{name}.jpg', 'image/jpeg',
                                        sys.getsizeof(img_output), 'utf-8')
        return img_file

    def test_cleanup_unused_files(self):
        album = self.create_album()
        album.cover = self.create_image('album_cover_img')
        album.save()
        album_cover_path = album.cover.path

        album.delete()
        self.assertTrue(default_storage.exists(album_cover_path))

        cleanup_unused_files()
        self.assertFalse(default_storage.exists(album_cover_path))