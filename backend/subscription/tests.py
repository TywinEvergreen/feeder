from django.urls import reverse

from user.tests import AuthorizedAPITestCase
from .models import Subscription


class SubscriptionTest(AuthorizedAPITestCase):

    def test_create_subscription(self):
        artist = self.create_artist()
        response = self.client.post(reverse('subscriptions'), {
            'author_type_str': 'artist',
            'author_id': artist.id
        })
        print(response.data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['author_type'], 'artist')
        self.assertEqual(response.data['author_object']['id'], artist.id)

        channel = self.create_channel()
        response = self.client.post(reverse('subscriptions'), {
            'author_type_str': 'channel',
            'author_id': channel.id
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['author_type'], 'channel')
        self.assertEqual(response.data['author_object']['id'], channel.id)
