from django.urls import reverse
from rest_framework.test import APITestCase

from spotify.tests.factories import ArtistFactory
from subscription.tests.factories import ArtistSubscriptionFactory, ChannelSubscriptionFactory
from user.tests.factories import UserFactory
from youtube.tests.factories import ChannelFactory


class ArtistSubscriptionViewSetTest(APITestCase):
    def setUp(self) -> None:
        self.user = UserFactory()
        self.artist = ArtistFactory()
        self.subscription = ArtistSubscriptionFactory(artist=self.artist, subscriber=self.user)

    def test_create_artist_subscription(self):
        self.client.force_login(self.user)
        url = reverse('subscription:artist-subscription-list')
        response = self.client.post(url, {
            'artist': self.artist.pk
        })

        self.assertEqual(response.status_code, 201)

    def test_delete_artist_subscription(self):
        self.client.force_login(self.user)
        url = reverse('subscription:artist-subscription-detail', kwargs={'pk': self.subscription.pk})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, 204)
        self.assertFalse(self.user.artist_subscriptions.exists())


class ChannelSubscriptionViewSetTest(APITestCase):
    def setUp(self) -> None:
        self.user = UserFactory()
        self.channel = ChannelFactory()
        self.subscription = ChannelSubscriptionFactory(channel=self.channel, subscriber=self.user)

    def test_create_channel_subscription(self):
        self.client.force_login(self.user)
        url = reverse('subscription:channel-subscription-list')
        response = self.client.post(url, {
            'channel': self.channel.pk
        })
        self.assertEqual(response.status_code, 201)

    def test_delete_artist_subscription(self):
        self.client.force_login(self.user)
        url = reverse('subscription:channel-subscription-detail', kwargs={'pk': self.subscription.pk})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, 204)
        self.assertFalse(self.user.channel_subscriptions.exists())
