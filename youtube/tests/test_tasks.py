from django.test import TestCase
from dateutil.parser import parse
import pytz

from youtube.models import VideoNotification
from youtube.tests.factories import ChannelFactory
from youtube.tasks import get_new_videos


class TestTasks(TestCase):
    def setUp(self):
        self.channel = ChannelFactory(youtube_id='UC6bTF68IAV1okfRfwXIP1Cg')

    def test_get_new_videos(self):
        self.channel.video.release_datetime = pytz.utc.localize(parse('1/1/1500 00:00'))
        self.channel.video.save()

        get_new_videos()
        self.channel.refresh_from_db()

        self.assertTrue(
            VideoNotification.objects.filter(album=self.channel.album).exists()
        )
        self.assertNotEqual(
            self.channel.video.release_datetime,
            pytz.utc.localize(parse('1/1/1500 00:00'))
        )
