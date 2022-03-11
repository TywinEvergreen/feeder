from django.db import models

from feeder.settings import AUTH_USER_MODEL
from spotify.models import Artist
from youtube.models import Channel


class DefaultSubscription(models.Model):
    datetime_committed = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ["-datetime_committed"]


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


class ChannelSubscription(DefaultSubscription):
    channel = models.ForeignKey(
        Channel, on_delete=models.CASCADE, related_name="subscriptions"
    )
    subscriber = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="channel_subscriptions"
    )

    def __str__(self):
        return f"Subscription of user #{self.subscriber.id} to channel #{self.channel.id}"

    class Meta:
        verbose_name = "Channel subscription"
        verbose_name_plural = "Channel subscription"
        unique_together = ["channel", "subscriber"]
