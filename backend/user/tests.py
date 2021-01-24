from django.urls import reverse

from utils.tests import AuthorizedAPITestCase


class TestUser(AuthorizedAPITestCase):

    def test_user_update(self):
        response = self.client.patch(reverse('user'), {
            'email': 'nope@gmail.com'
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['email'], 'nope@gmail.com')