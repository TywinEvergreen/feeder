from django.urls import reverse
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType

from rest_framework.test import APITestCase
from dateutil.parser import parse

from feeder.settings import TEST_USER_PASSWORD
from feeder.utils import delete_related_files
from spotify.models import Artist, Album, ArtistSubscription, AlbumNotification
from youtube.models import Channel, Video, ChannelSubscription, VideoNotification
from .generators import generate_random_email
from .models import User


class AuthorizedAPITestCase(APITestCase):
    """
    TestCase для авторизованных запросов
    """

    def setUp(self):
        user = self.create_superuser(generate_random_email())
        auth_response = self.authenticate(user.email, TEST_USER_PASSWORD)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + auth_response.data['auth_token'])
        self.user = User.objects.last()

    def create_artist(self, spotify_id='1'):
        artist = Artist.objects.create(name='test_artist', spotify_id=spotify_id)
        return artist

    def create_album(self, artist=None, spotify_id='1'):
        assert not artist or type(artist) is Artist
        artist = artist or self.create_artist()
        album = Album.objects.create(name='test_album', spotify_id=spotify_id,
                                     artist=artist, release_date=timezone.now().date())
        return album

    def create_channel(self, youtube_id='1'):
        channel = Channel.objects.create(name='test_channel', youtube_id=youtube_id)
        return channel

    def create_video(self, channel=None, youtube_id='1'):
        assert not channel or isinstance(channel, Channel)
        channel = channel or self.create_channel()
        video = Video.objects.create(name='test_video', youtube_id=youtube_id,
                                     channel=channel, release_datetime=timezone.now())
        return video

    def create_artist_subscription(self, artist):
        assert isinstance(artist, Artist)
        subscription = ArtistSubscription.objects.create(
            artist=artist,
            subscriber=self.user
        )
        return subscription

    def create_channel_subscription(self, channel):
        assert isinstance(channel, Channel)
        subscription = ChannelSubscription.objects.create(
            channel=channel,
            subscriber=self.user
        )
        return subscription

    def create_album_notification(self, album):
        assert isinstance(album, Album)
        notification = AlbumNotification.objects.create(album=album)
        return notification

    def create_video_notification(self, video):
        assert isinstance(video, Video)
        notification = VideoNotification.objects.create(video=video)
        return notification

    def create_superuser(self, email, password=TEST_USER_PASSWORD):
        superuser = User.objects.create_superuser(email, password)
        return superuser

    def authenticate(self, email, password=TEST_USER_PASSWORD):
        auth_response = self.client.post('/auth/token/login/', {
            'email': email,
            'password': password
        })
        return auth_response