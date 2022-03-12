from django.db import models

from feeder.settings import AUTH_USER_MODEL
from spotify.models import Artist
from subscription.models.base import DefaultSubscription


class ArtistSubscription(DefaultSubscription):
    artist = models.ForeignKey(
        Artist, on_delete=models.CASCADE, related_name="subscriptions"
    )
    subscriber = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="artist_subscriptions"
    )

    def __str__(self):
        return f"Subscription of user #{self.subscriber.id} to artist #{self.artist.id}"

    class Meta:
        verbose_name = "Artist subscription"
        verbose_name_plural = "Artist subscriptions"
        unique_together = ["artist", "subscriber"]
