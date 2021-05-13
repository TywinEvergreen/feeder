from django.urls import reverse
from rest_framework.test import APITestCase

from subscription.tests.factories import ChannelSubscriptionFactory
from user.tests.factories import UserFactory
from youtube.tests.factories import ChannelFactory, VideoFactory, VideoNotificationFactory
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
        self.user1 = UserFactory()
        self.user2 = UserFactory()
        self.channel = ChannelFactory()
        self.video = VideoFactory(channel=self.channel)

    def test_get_video_notifications(self):
        video = VideoNotificationFactory(
            video=self.video,
            received_by=[self.user1, self.user2],
            discarded_by=[self.user2]
        )
        print(video.received_by.all())
        print(video.discarded_by.all())

        url = reverse('youtube:video-notifications-list')

        self.client.force_login(self.user1)
        response1 = self.client.get(url)

        self.client.force_login(self.user2)
        response2 = self.client.get(url)
        print(response1.data)
        print(response2.data)

        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response1.data['count'], 1)
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(response2.data['count'], 0)
