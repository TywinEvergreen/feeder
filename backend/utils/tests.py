import os
import shutil

from django.test.runner import DiscoverRunner
from django.utils import timezone

from rest_framework.test import APITestCase
from rest_framework.response import Response

from feeder.settings import MEDIA_ROOT, TEST_USER_PASSWORD
from spotify.models import Artist, Album
from youtube.models import Channel, Video
from subscription.models import ArtistSubscription, ChannelSubscription
from user.models import User
from .generators import generate_random_email


class CustomTestRunner(DiscoverRunner):
    """
    Это тестировщик удаляет директорию
    media/testing после выполнения тестов
    """

    def teardown_test_environment(self, *args, **kwargs):
        if os.path.isdir(os.path.join(MEDIA_ROOT, 'testing')):
            shutil.rmtree(os.path.join(MEDIA_ROOT, 'testing'))
        super(CustomTestRunner, self).teardown_test_environment(*args, **kwargs)


class AuthorizedAPITestCase(APITestCase):
    """
    TestCase для авторизованных запросов
    """

    def setUp(self):
        user = self.create_superuser(generate_random_email())
        auth_response = self.authenticate(user.email, TEST_USER_PASSWORD)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + auth_response.data['auth_token'])
        self.user = User.objects.last()

    def create_artist(self, spotify_id='1') -> Artist:
        artist = Artist.objects.create(name='test_artist', spotify_id=spotify_id)
        return artist

    def create_album(self, artist=None, spotify_id='1') -> Album:
        artist = artist or self.create_artist()
        album = Album.objects.create(name='test_album', spotify_id=spotify_id,
                                     artist=artist, release_datetime=timezone.now())
        return album

    def create_channel(self, youtube_id='1') -> Channel:
        channel = Channel.objects.create(name='test_channel', youtube_id=youtube_id)
        return channel

    def create_video(self, channel=None, youtube_id='1') -> Video:
        channel = channel or self.create_channel()
        video = Video.objects.create(name='test_video', youtube_id=youtube_id,
                                     channel=channel, release_datetime=timezone.now())
        return video

    def create_artist_subscription(self, artist:Artist) -> ArtistSubscription:
        subscription = ArtistSubscription.objects.create(
            artist=artist,
            subscriber=self.user
        )
        return subscription

    def create_channel_subscription(self, channel:Channel) -> ChannelSubscription:
        subscription = ChannelSubscription.objects.create(
            channel=channel,
            subscriber=self.user
        )
        return subscription

    def create_superuser(self, email:str, password=TEST_USER_PASSWORD) -> User:
        superuser = User.objects.create_superuser(email, password) # type: ignore
        return superuser

    def authenticate(self, email:str, password=TEST_USER_PASSWORD) -> Response:
        auth_response = self.client.post('/auth/token/login/', {
            'email': email,
            'password': password
        })
        return auth_response
