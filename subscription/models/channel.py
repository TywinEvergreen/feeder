from django.db import models

from feeder.settings import AUTH_USER_MODEL
from subscription.models.base import DefaultSubscription
from youtube.models import Channel


class ChannelSubscription(DefaultSubscription):
    channel = models.ForeignKey(
        Channel, on_delete=models.CASCADE, related_name="subscriptions"
    )
    subscriber = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="channel_subscriptions"
    )

    def __str__(self):
        return (
            f"Subscription of user #{self.subscriber.id} to channel #{self.channel.id}"
        )

    class Meta:
        verbose_name = "Channel subscription"
        verbose_name_plural = "Channel subscription"
        unique_together = ["channel", "subscriber"]
