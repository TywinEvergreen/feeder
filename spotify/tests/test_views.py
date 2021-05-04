from django.urls import reverse
from rest_framework.test import APITestCase

from spotify.tests.factories import ArtistFactory, AlbumFactory
from spotify.models import Artist
from subscription.tests.factories import ArtistSubscriptionFactory
from user.tests.factories import UserFactory


class ArtistViewSetTest(APITestCase):
    def setUp(self) -> None:
        self.user = UserFactory()

    def test_create_artist(self):
        self.client.force_login(self.user)
        url = reverse('spotify:artist-list')
        response = self.client.post(url, {
            'spotify_id': '123',
            'name': 'test',
        })

        self.assertEqual(response.status_code, 201)
        self.assertTrue(
            Artist.objects.filter(spotify_id='123', name='test').exists()
        )


class NewAlbumsViewSetTest(APITestCase):
    def setUp(self) -> None:
        self.user = UserFactory()
        self.artist1 = ArtistFactory()
        self.artist2 = ArtistFactory()

    def test_get_new_albums(self):
        AlbumFactory(artist=self.artist1)
        ArtistSubscriptionFactory(artist=self.artist2, subscriber=self.user)
        AlbumFactory(artist=self.artist2)

        self.client.force_login(self.user)
        url = reverse('spotify:new-albums-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['count'], 1)
