from django.test import TestCase

from subscription.tests.factories import ChannelSubscriptionFactory
from user.tests.factories import UserFactory
from utils.decorators import signal_decorator
from youtube.tests.factories import VideoFactory, ChannelFactory
from youtube.models import VideoNotification


class SignalTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory()
        self.channel = ChannelFactory()
        self.subscription = ChannelSubscriptionFactory(channel=self.channel, subscriber=self.user)

    @signal_decorator('youtube.signals.create_video_notifications')
    def test_notification_is_created_after_video_creation(self):
        VideoFactory(channel=self.channel)
        notifications = VideoNotification.objects.filter(received_by=self.user)

        self.assertEqual(notifications.count(), 1)
