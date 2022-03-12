from django.test import TestCase

from subscription.tests.factories import ArtistSubscriptionFactory
from user.tests.factories import UserFactory
from utils.decorators import signal_decorator
from spotify.tests.factories import AlbumFactory, ArtistFactory
from spotify.models import AlbumNotification


class SignalTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory()
        self.artist = ArtistFactory()
        self.subscription = ArtistSubscriptionFactory(
            artist=self.artist, subscriber=self.user
        )

    @signal_decorator("spotify.signals.create_album_notifications")
    def test_notification_is_created_after_album_creation(self):
        AlbumFactory(artist=self.artist)
        notifications = AlbumNotification.objects.filter(received_by=self.user)
        self.assertEqual(notifications.count(), 1)
