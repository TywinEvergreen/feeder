from django.urls import reverse

from user.tests import AuthorizedAPITestCase
from spotify.models import Artist
from youtube.models import Channel
from .models import Subscription


class SubscriptionTest(AuthorizedAPITestCase):

    def test_create_subscription(self):
        author = self.create_artist()
        subscription = self.create_subscription('artist', author.id)
        self.assertEqual(self.user.subscriptions.last(), subscription)

    def test_api_create_subscription(self):
        artist = self.create_artist()
        response = self.client.post(reverse('subscriptions'), {
            'content_type_str': 'artist',
            'object_id': artist.id
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['content_type'], 'artist')
        self.assertEqual(response.data['author']['id'], artist.id)

        channel = self.create_channel()
        response = self.client.post(reverse('subscriptions'), {
            'content_type_str': 'channel',
            'object_id': channel.id
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['content_type'], 'channel')
        self.assertEqual(response.data['author']['id'], channel.id)

    def test_get_subscriptions(self):
        author1 = self.create_artist()
        author2 = self.create_channel()
        subscription1 = self.create_subscription('artist', author1.id)
        subscription2 = self.create_subscription('channel', author2.id)

        response = self.client.get(reverse('subscriptions'))
        self.assertEqual(response.data['results'][0]['content_type'], 'channel')
        self.assertEqual(response.data['results'][0]['id'], subscription2.id)
        self.assertEqual(response.data['results'][1]['content_type'], 'artist')
        self.assertEqual(response.data['results'][1]['id'], subscription1.id)
