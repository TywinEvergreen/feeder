from django.db.models.signals import post_save
from django.dispatch import receiver

from subscription.models import ChannelSubscription
from youtube.models import Video, VideoNotification


@receiver(post_save, sender=Video)
def create_video_notifications(sender, instance, created, **kwargs):
    if created:
        subscribers = ChannelSubscription.objects.filter(channel=instance.channel).values_list('subscriber', flat=True)
        if subscribers:
            notification = VideoNotification.objects.create(video=instance)
            notification.to.set(subscribers)
