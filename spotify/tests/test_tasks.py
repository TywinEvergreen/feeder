from django.test import TestCase

from subscription.tests.factories import ArtistSubscriptionFactory
from user.tests.factories import UserFactory
from spotify.tests.factories import ArtistFactory
from spotify.tasks import get_new_albums


class TestTasks(TestCase):
    def setUp(self):
        self.artist = ArtistFactory(spotify_id='3o2dn2O0FCVsWDFSh8qxgG')
        self.subscriber = UserFactory()
        ArtistSubscriptionFactory(artist=self.artist, subscriber=self.subscriber)

    def test_get_new_videos(self):
        get_new_albums()
        self.artist.refresh_from_db()

        self.assertTrue(hasattr(self.artist, 'album'))
