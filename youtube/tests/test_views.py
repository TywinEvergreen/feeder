from django.urls import reverse
from rest_framework.test import APITestCase

from subscription.tests.factories import ChannelSubscriptionFactory
from user.tests.factories import UserFactory
from youtube.tests.factories import ChannelFactory, VideoFactory
from youtube.models import Channel


class ChannelViewSetTest(APITestCase):
    def setUp(self) -> None:
        self.user = UserFactory()

    def test_create_channel(self):
        self.client.force_login(user=self.user)
        url = reverse('youtube:channel-list')
        response = self.client.post(url, {
            'youtube_id': '123',
            'name': 'test',
        })

        self.assertEqual(response.status_code, 201)
        self.assertTrue(
            Channel.objects.filter(youtube_id='123', name='test').exists()
        )


class NewVideosViewSetTest(APITestCase):
    def setUp(self) -> None:
        self.user = UserFactory()
        self.channel1 = ChannelFactory()
        self.channel2 = ChannelFactory()

    def test_get_new_videos(self):
        VideoFactory(channel=self.channel1)
        ChannelSubscriptionFactory(channel=self.channel2, subscriber=self.user)
        VideoFactory(channel=self.channel2)

        self.client.force_login(self.user)
        url = reverse('youtube:new-videos-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['count'], 1)
