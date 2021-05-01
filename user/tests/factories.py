import factory

from user.models import User


class UserFactory(factory.django.DjangoModelFactory):
    email = factory.Faker("email")

    class Meta:
        model = User
