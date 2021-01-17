from django.urls import reverse

import pytz
from dateutil.parser import parse

from feeder.settings import SPOTIFY
from feeder.utils import delete_related_files
from user.tests import AuthorizedAPITestCase
from spotify.models import Album
from youtube.models import Video
from .tasks import get_new_albums, get_new_videos


class TestSpotify(AuthorizedAPITestCase):

    def test_connection(self):
        response = SPOTIFY.artist('3o2dn2O0FCVsWDFSh8qxgG')
        self.assertEqual(response['id'], '3o2dn2O0FCVsWDFSh8qxgG')


class TestAlbumNotification(AuthorizedAPITestCase):

    def test_get_album_notifications(self):
        artist = self.create_artist()
        self.create_artist_subscription(artist)
        album = self.create_album(artist)
        self.create_album_notification(album)

        response = self.client.get(reverse('album-notifications'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['count'], 1)


class TestVideoNotification(AuthorizedAPITestCase):

    def test_get_video_notifications(self):
        channel1 = self.create_channel()
        channel2 = self.create_channel('2')
        video1 = self.create_video(channel1)
        self.create_video_notification(video1)

        response = self.client.get(reverse('video-notifications'))
        self.assertEqual(response.data['count'], 0)

        self.create_channel_subscription(channel1)
        self.create_channel_subscription(channel2)
        video2 = self.create_video(channel2, '2')
        self.create_video_notification(video2)

        response = self.client.get(reverse('video-notifications'))
        self.assertEqual(response.data['count'], 1)

        video1.delete()
        video1 = self.create_video(channel1)
        self.create_video_notification(video1)

        response = self.client.get(reverse('video-notifications'))
        self.assertEqual(response.data['count'], 2)


class TestTasks(AuthorizedAPITestCase):

    def tearDown(self):
        for album in Album.objects.all():
            delete_related_files(album)
        for video in Video.objects.all():
            delete_related_files(video)

    def test_get_new_albums(self):
        artist = self.create_artist(spotify_id='3o2dn2O0FCVsWDFSh8qxgG')

        get_new_albums()
        artist.refresh_from_db()
        self.assertTrue(hasattr(artist, 'album'))
        self.assertTrue(artist.album.cover)

        artist.album.release_date = pytz.utc.localize(parse('1/1/1500'))
        artist.album.save()

        get_new_albums()
        artist.refresh_from_db()
        self.assertNotEqual(artist.album.release_date, pytz.utc.localize(parse('1/1/1500')))

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