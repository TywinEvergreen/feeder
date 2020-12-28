from django.urls import reverse
from django.contrib.contenttypes.models import ContentType

from user.tests import AuthorizedAPITestCase
from .models import Notification


class NotificationTest(AuthorizedAPITestCase):

    def test_get_notification(self):
        artist = self.create_artist()
        youtuber = self.create_channel()

        album = self.create_album(artist)
        video = self.create_video(youtuber)

        Notification.objects.create(
            content_type=ContentType.objects.get_for_model(album),
            object_id=album.pk
        )
        Notification.objects.create(
            content_type=ContentType.objects.get_for_model(video),
            object_id=video.pk
        )

        self.user.followed_artists.add(artist)
        response = self.client.get(reverse('notifications'))
        self.assertEqual(response.data['count'], 1)

        self.user.followed_channels.add(youtuber)
        response = self.client.get(reverse('notifications'))
        self.assertEqual(response.data['count'], 2)

        self.user.followed_artists.clear()
        self.user.followed_channels.clear()
        response = self.client.get(reverse('notifications'))
        self.assertEqual(response.data['count'], 0)
