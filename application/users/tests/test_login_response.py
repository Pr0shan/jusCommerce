from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginResponseTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="loginuser@example.com",
            full_name="loginuser",
            role="customer",
            password="strongpassword123"
        )
        return super().setUp()
    
    def test_user_can_login_and_get_token(self):
        url = reverse('login')
        data = {
            "email": "loginuser@example.com",
            "password": "strongpassword123"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)