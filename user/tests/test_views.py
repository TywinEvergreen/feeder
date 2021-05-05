from django.urls import reverse
from rest_framework.test import APITestCase

from user.tests.factories import UserFactory


class TestUser(APITestCase):
    def setUp(self) -> None:
        self.user = UserFactory()

    def test_user_update(self):
        self.client.force_login(self.user)
        url = reverse('user:detail')
        response = self.client.patch(url, {
            'email': 'test@gmail.com'
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['email'], 'test@gmail.com')
