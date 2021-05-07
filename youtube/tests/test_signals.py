from django.test import TestCase

from subscription.tests.factories import ChannelSubscriptionFactory
from user.tests.factories import UserFactory
from youtube.tests.factories import VideoFactory, ChannelFactory
from youtube.models import VideoNotification


class SignalTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory()
        self.channel = ChannelFactory()
        self.subscription = ChannelSubscriptionFactory(channel=self.channel, subscribers=[self.user])

    def test_notification_is_created_after_video_creation(self):
        VideoFactory(channel=self.channel)
        self.assertTrue(VideoNotification.objects.exists())
        self.assertEqual(VideoNotification.objects.count(), 1)
