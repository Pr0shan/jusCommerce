from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APITestCase

User = get_user_model()

class RegistrationTestCase(APITestCase):
    def test_user_can_register(self):
        url = reverse('register_user')
        data = {
            "email": 'testuser@example.com',
            'full_name': 'Test User',
            'password': 'strongpassword123',
            'password2': 'strongpassword123',
            'role': 'customer'
        }

        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().email, 'testuser@example.com')

