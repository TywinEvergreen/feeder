from user.tests import AuthorizedAPITestCase
from .models import Subscription


class SubscriptionTest(AuthorizedAPITestCase):

    def test_create_subscription(self):
        subscription = Subscription.objects.create()