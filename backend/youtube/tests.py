from django.urls import reverse
from django.utils import timezone

from dateutil.parser import parse
import pytz

from user.tests import AuthorizedAPITestCase
from feeder.settings import YOUTUBE
from feeder.utils import delete_related_files
from .tasks import get_new_videos
from .models import Video


class Youtube(AuthorizedAPITestCase):

    def tearDown(self):
        for video in Video.objects.all():
            delete_related_files(video)

    def test_create_artist(self):
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

    def test_get_new_videos(self):
        channel = self.create_channel(youtube_id='UC6bTF68IAV1okfRfwXIP1Cg')

        get_new_videos()
        channel.refresh_from_db()
        self.assertTrue(hasattr(channel, 'video'))
        self.assertTrue(channel.video.cover)

        channel.video.release_date = pytz.utc.localize(parse('1/1/1500 00:00'))
        channel.video.save()

        get_new_videos()
        channel.refresh_from_db()
        self.assertNotEqual(channel.video.release_date,
                            pytz.utc.localize(parse('1/1/1500 00:00')))


