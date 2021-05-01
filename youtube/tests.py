from django.urls import reverse
from dateutil.parser import parse
import pytz

from utils.tests import AuthorizedAPITestCase
from youtube.tasks import get_new_videos


class TestChannel(AuthorizedAPITestCase):

    def test_create_channel(self):
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
        channel1 = self.create_channel()
        channel2 = self.create_channel('2')
        video1 = self.create_video(channel1)

        response = self.client.get(reverse('new-videos'))
        self.assertEqual(response.data['count'], 0)

        self.create_channel_subscription(channel1)
        self.create_channel_subscription(channel2)
        video2 = self.create_video(channel2, '2')

        response = self.client.get(reverse('new-videos'))
        self.assertEqual(response.data['count'], 1)

        video1.delete()
        video1 = self.create_video(channel1)

        response = self.client.get(reverse('new-videos'))
        self.assertEqual(response.data['count'], 2)


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