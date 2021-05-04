import factory
from django.utils import timezone

from spotify.models import Artist, Album


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
