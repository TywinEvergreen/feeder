import factory
from django.utils import timezone

from spotify.models import Artist, Album, AlbumNotification


class ArtistFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("word")
    spotify_id = factory.Faker("word")

    class Meta:
        model = Artist


class AlbumFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("word")
    spotify_id = factory.Faker("word")
    artist = factory.SubFactory(ArtistFactory)

    type = factory.Faker(
        "random_element", elements=[x[0] for x in Album.TYPE_CHOICES]
    )

    release_datetime = factory.Faker(
        "date_time_this_decade",
        tzinfo=timezone.get_current_timezone(),
        after_now=True
    )

    class Meta:
        model = Album


class AlbumNotificationFactory(factory.django.DjangoModelFactory):
    album = factory.SubFactory(AlbumFactory)

    class Meta:
        model = AlbumNotification

    @factory.post_generation
    def received_by(self, create, extracted, **kwargs):
        if extracted:
            for user in extracted:
                self.received_by.add(user)

    @factory.post_generation
    def discarded_by(self, create, extracted, **kwargs):
        if extracted:
            for user in extracted:
                self.discarded_by.add(user)
