from django.test import TestCase
from dateutil.parser import parse
import pytz

from youtube.tests.factories import ChannelFactory
from youtube.tasks import get_new_videos


class TestTasks(TestCase):
    def setUp(self):
        self.channel = ChannelFactory(youtube_id='UC6bTF68IAV1okfRfwXIP1Cg')

    def test_get_new_videos(self):
        self.assertFalse(hasattr(self.channel, 'video'))

        get_new_videos()
        self.channel.refresh_from_db()

        self.assertTrue(hasattr(self.channel, 'video'))
