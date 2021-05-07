import factory

from subscription.models import ArtistSubscription, ChannelSubscription
from spotify.tests.factories import ArtistFactory
from user.tests.factories import UserFactory
from youtube.tests.factories import ChannelFactory


class ArtistSubscriptionFactory(factory.django.DjangoModelFactory):
    artist = factory.SubFactory(ArtistFactory)

    @factory.post_generation
    def subscribers(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for subscribers in extracted:
                self.subscribers.add(subscribers)

    class Meta:
        model = ArtistSubscription


class ChannelSubscriptionFactory(factory.django.DjangoModelFactory):
    channel = factory.SubFactory(ChannelFactory)
    subscribers = factory.SubFactory(UserFactory, many=True)

    class Meta:
        model = ChannelSubscription
