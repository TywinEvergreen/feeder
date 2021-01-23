from django.urls import reverse

from user.tests import AuthorizedAPITestCase


class TestArtistSubscription(AuthorizedAPITestCase):

    def test_create_artist_subscription(self):
        artist = self.create_artist()
        response = self.client.post(reverse('subscribe-artist'), {
            'artist': artist.pk
        })
        self.assertEqual(response.status_code, 201)

    def test_delete_artist_subscription(self):
        artist = self.create_artist()
        subscription = self.create_artist_subscription(artist)
        response = self.client.delete(reverse(
            'destroy-artist-subscription',
            kwargs={'pk': subscription.pk}
        ))
        self.assertEqual(response.status_code, 204)
        self.assertFalse(self.user.artist_subscriptions.exists())

class TestChannelSubscription(AuthorizedAPITestCase):

    def test_create_channel_subscription(self):
        channel = self.create_channel()
        response = self.client.post(reverse('subscribe-channel'), {
            'channel': channel.pk
        })
        print(response.data)
        self.assertEqual(response.status_code, 201)

    def test_delete_artist_subscription(self):
        channel = self.create_channel()
        subscription = self.create_channel_subscription(channel)
        response = self.client.delete(reverse(
            'destroy-channel-subscription',
            kwargs={'pk': subscription.pk}
        ))
        self.assertEqual(response.status_code, 204)
        self.assertFalse(self.user.channel_subscriptions.exists())