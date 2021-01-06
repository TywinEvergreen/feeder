from django.urls import reverse
from django.contrib.contenttypes.models import ContentType

from user.tests import AuthorizedAPITestCase
from .models import Notification


class NotificationTest(AuthorizedAPITestCase):

    def test_get_notification(self):
        artist = self.create_artist()
        channel = self.create_channel()
        album = self.create_album(artist)
        video = self.create_video(channel)

        Notification.objects.create(
            content_type=ContentType.objects.get_for_model(album),
            object_id=album.pk
        )

        self.create_subscription('artist', artist.id)
        self.create_subscription('channel', channel.id)

        Notification.objects.create(
            content_type=ContentType.objects.get_for_model(video),
            object_id=video.pk
        )

        response = self.client.get(reverse('notifications'))
        print(response.data)
        # self.assertEqual(response.data['count'], 1)
