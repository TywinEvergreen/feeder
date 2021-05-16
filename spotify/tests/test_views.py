from django.urls import reverse
from rest_framework.test import APITestCase

from user.tests.factories import UserFactory
from spotify.tests.factories import ArtistFactory, AlbumFactory, AlbumNotificationFactory
from spotify.models import Artist


class ArtistViewSetTest(APITestCase):
    def setUp(self) -> None:
        self.user = UserFactory()

    def test_create_channel(self):
        self.client.force_login(user=self.user)
        url = reverse('spotify:artist-list')
        response = self.client.post(url, {
            'spotify_id': '123',
            'name': 'test',
        })

        self.assertEqual(response.status_code, 201)
        self.assertTrue(
            Artist.objects.filter(spotify_id='123', name='test').exists()
        )


class NewVideosViewSetTest(APITestCase):
    def setUp(self) -> None:
        self.user1 = UserFactory()
        self.user2 = UserFactory()
        self.artist = ArtistFactory()
        self.album = AlbumFactory(artist=self.artist)

    def test_get_video_notifications(self):
        AlbumNotificationFactory(
            album=self.album,
            received_by=[self.user1, self.user2],
            discarded_by=[self.user2]
        )

        url = reverse('spotify:album-notifications-list')

        self.client.force_login(self.user1)
        response1 = self.client.get(url)

        self.client.force_login(self.user2)
        response2 = self.client.get(url)

        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response1.data['count'], 1)
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(response2.data['count'], 0)
