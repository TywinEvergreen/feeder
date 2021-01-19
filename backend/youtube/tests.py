from django.urls import reverse

from user.tests import AuthorizedAPITestCase


class TestChannel(AuthorizedAPITestCase):

    def test_create_channel(self):
        response = self.client.post(reverse('channel'), {
            'youtube_id': '123',
            'name': 'test'
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['youtube_id'], '123')
        self.assertEqual(response.data['name'], 'test')

        response = self.client.post(reverse('channel'), {
            'youtube_id': '123'
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['youtube_id'], '123')
        self.assertEqual(response.data['name'], 'test')