import factory

from youtube.models import Channel, Video


class ChannelFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("word")
    youtube_id = factory.Faker("word")

    class Meta:
        model = Channel


class VideoFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("word")
    youtube_id = factory.Faker("word")
    channel = factory.SubFactory(ChannelFactory)
    release_datetime = factory.Faker("date_time_this_decade", before_now=True, after_now=True)

    class Meta:
        model = Video
