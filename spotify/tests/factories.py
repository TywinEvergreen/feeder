import factory

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

    release_datetime = factory.Faker("date_time_this_decade", before_now=True, after_now=True)

    class Meta:
        model = Album
