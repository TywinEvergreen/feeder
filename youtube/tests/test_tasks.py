from django.test import TestCase

from subscription.tests.factories import ChannelSubscriptionFactory
from user.tests.factories import UserFactory
from youtube.tests.factories import ChannelFactory
from youtube.tasks import get_new_videos


class TestTasks(TestCase):
    def setUp(self):
        self.channel = ChannelFactory(youtube_id='UC6bTF68IAV1okfRfwXIP1Cg')
        self.subscriber = UserFactory()
        ChannelSubscriptionFactory(channel=self.channel, subscriber=self.subscriber)

    def test_get_new_videos(self):
        get_new_videos()
        self.channel.refresh_from_db()

        self.assertTrue(hasattr(self.channel, 'video'))
