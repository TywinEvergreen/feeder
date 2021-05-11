import factory

from subscription.models import ArtistSubscription, ChannelSubscription
from spotify.tests.factories import ArtistFactory
from user.tests.factories import UserFactory
from youtube.tests.factories import ChannelFactory


class ArtistSubscriptionFactory(factory.django.DjangoModelFactory):
    artist = factory.SubFactory(ArtistFactory)
    subscriber = factory.SubFactory(UserFactory)

    class Meta:
        model = ArtistSubscription


class ChannelSubscriptionFactory(factory.django.DjangoModelFactory):
    channel = factory.SubFactory(ChannelFactory)
    subscriber = factory.SubFactory(UserFactory)

    class Meta:
        model = ChannelSubscription
