from django.urls import reverse

import pytz
from dateutil.parser import parse

from utils.tests import AuthorizedAPITestCase
from .models import Artist, Album
from .tasks import get_new_albums


class TestArtist(AuthorizedAPITestCase):

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