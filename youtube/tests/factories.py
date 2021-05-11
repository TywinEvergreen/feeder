import factory
from django.utils import timezone

from youtube.models import Channel, Video, VideoNotification


class ChannelFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("word")
    youtube_id = factory.Faker("word")

    class Meta:
        model = Channel


class VideoFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("word")
    youtube_id = factory.Faker("word")
    channel = factory.SubFactory(ChannelFactory)
    release_datetime = factory.Faker(
        "date_time_this_decade",
        tzinfo=timezone.get_current_timezone(),
        after_now=True
    )

    class Meta:
        model = Video


class VideoNotificationFactory(factory.django.DjangoModelFactory):
    video = factory.SubFactory(VideoFactory)

    class Meta:
        model = VideoNotification
