from django.urls import reverse

from user.tests import AuthorizedAPITestCase


class TestArtistSubscription(AuthorizedAPITestCase):

    def test_create_artist_subscription(self):
        artist = self.create_artist()
        response = self.client.post(reverse('subscribe-artist'), {
            'artist': artist.pk
        })
        self.assertEqual(response.status_code, 201)


class TestChannelSubscription(AuthorizedAPITestCase):

    def test_create_channel_subscription(self):
        channel = self.create_channel()
        response = self.client.post(reverse('subscribe-channel'), {
            'channel': channel.pk
        })
        self.assertEqual(response.status_code, 201)