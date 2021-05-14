from django.db.models.signals import post_save
from django.dispatch import receiver

from subscription.models import ArtistSubscription
from spotify.models import Album, AlbumNotification


@receiver(post_save, sender=Album)
def create_album_notifications(sender, instance, created, **kwargs):
    if created:
        subscribers = ArtistSubscription.objects.filter(artist=instance.artist).values_list('subscriber', flat=True)
        if subscribers:
            notification = AlbumNotification.objects.create(album=instance)
            notification.received_by.set(subscribers)
