from django.urls import reverse
from rest_framework.test import APITestCase

import pytz
from dateutil.parser import parse

from subscription.tests.factories import ChannelSubscriptionFactory
from user.tests.factories import UserFactory
from youtube.tests.factories import ChannelFactory, VideoFactory
from youtube.models import Channel, Video
from spotify.tasks import get_new_albums


class ChannelViewSetTest(APITestCase):
    def setUp(self) -> None:
        self.user = UserFactory()
        self.channel = ChannelFactory()

    def test_create_channel(self):
        self.client.force_login(self.user)
        url = reverse('youtube:channel-detail')
        response = self.client.post(url, {
            'youtube_id': '123',
            'name': 'test',
        })

        self.assertEqual(response.status_code, 201)
        self.assertTrue(
            Channel.objects.filter(youtube_id='123', name='test').exists()
        )

    def test_get_new_videos(self):
        VideoFactory(channel=self.channel)
        ChannelSubscriptionFactory(channel=self.channel, subscriber=self.user)
        VideoFactory(channel=self.channel)

        self.client.force_login(self.user)
        url = reverse('youtube:new-videos-list')
        response = self.client.get(url)

        self.assertEqual(response.data['count'], 1)
