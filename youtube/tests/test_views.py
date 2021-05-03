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

    def test_get_new_videos(self):
        channel1 = ChannelFactory()
        VideoFactory(channel=channel1)

        channel2 = ChannelFactory()
        ChannelSubscriptionFactory(channel=channel2, subscriber=self.user)
        VideoFactory(channel=channel2)

        self.client.force_login(user=self.user)
        url = reverse('youtube:new-videos-list')
        response = self.client.get(url)

        self.assertEqual(response.data['count'], 1)


class TestTasks(AuthorizedAPITestCase):

    def test_get_new_videos(self):
        channel = self.create_channel(youtube_id='UC6bTF68IAV1okfRfwXIP1Cg')

        get_new_videos()
        channel.refresh_from_db()
        self.assertTrue(hasattr(channel, 'video'))
        self.assertTrue(channel.video.cover)

        channel.video.release_datetime = pytz.utc.localize(parse('1/1/1500 00:00'))
        channel.video.save()

        get_new_videos()
        channel.refresh_from_db()
        self.assertNotEqual(channel.video.release_datetime,
                            pytz.utc.localize(parse('1/1/1500 00:00')))
