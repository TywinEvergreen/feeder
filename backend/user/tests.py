from django.urls import reverse
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType

from rest_framework.test import APITestCase
from dateutil.parser import parse

from feeder.settings import TEST_USER_PASSWORD
from feeder.utils import delete_related_files
from spotify.models import Artist, Album
from youtube.models import Channel, Video
from subscription.models import Subscription
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
        assert not artist or type(artist) is Artist, 'Укажите подходящего исполнителя'
        artist = artist or self.create_artist()
        album = Album.objects.create(name='test_album', spotify_id=spotify_id,
                                     artist=artist, release_date=parse('2010'))
        return album

    def create_channel(self, youtube_id='1'):
        channel = Channel.objects.create(name='test_channel', youtube_id=youtube_id)
        return channel

    def create_video(self, channel=None, youtube_id='1'):
        assert not channel or type(channel) is Channel, 'Укажите подходящего ютубера'
        channel = channel or self.create_channel()
        video = Video.objects.create(name='test_video', youtube_id=youtube_id,
                                     channel=channel, release_date=timezone.now())
        return video

    def create_subscription(self, author_type, author_id):
        subscription = Subscription.objects.create(
            content_type=ContentType.objects.get(model=author_type),
            object_id=author_id,
            subscriber=self.user
        )
        return subscription

    def create_api_user(self, email, password=TEST_USER_PASSWORD):
        response = self.client.post('/auth/users/', {
            'email': email,
            'password': password
        })
        return response

    def create_superuser(self, email, password=TEST_USER_PASSWORD):
        superuser = User.objects.create_superuser(email, password)
        return superuser

    def authenticate(self, email, password=TEST_USER_PASSWORD):
        auth_response = self.client.post('/auth/token/login/', {
            'email': email,
            'password': password
        })
        return auth_response


class DjoserTest(AuthorizedAPITestCase):

    def test_register_user(self):
        response = self.create_api_user('e@gmail.com')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['email'], 'e@gmail.com')

    def test_authenticate_user(self):
        reg_response = self.create_api_user('e@gmail.com')
        response = self.authenticate(reg_response.data['email'], TEST_USER_PASSWORD)
        self.assertEqual(response.status_code, 200)
