from django.urls import reverse
from django.contrib.contenttypes.models import ContentType

from user.tests import AuthorizedAPITestCase
from .models import Notification


class NotificationTest(AuthorizedAPITestCase):

    def test_get_notification(self):
        artist = self.create_artist()
        channel = self.create_channel()
        video = self.create_video(channel)
        Notification.objects.create(
            content_type=ContentType.objects.get(model='video'),
            object_id=video.pk
        )

        response = self.client.get(reverse('notifications'))
        self.assertEqual(response.data['count'], 0)

        self.create_subscription('artist', artist.id)
        self.create_subscription('channel', channel.id)

        album = self.create_album(artist)
        Notification.objects.create(
            content_type=ContentType.objects.get(model='album'),
            object_id=album.pk
        )

        response = self.client.get(reverse('notifications'))
        self.assertEqual(response.data['count'], 1)

        video.delete()
        video2 = self.create_video(channel, '2')
        Notification.objects.create(
            content_type=ContentType.objects.get(model='video'),
            object_id=video2.pk
        )

        response = self.client.get(reverse('notifications'))
        self.assertEqual(response.data['count'], 2)

