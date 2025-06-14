# TODO: Test
# 1. the product can be created
# 2. the product can only be created by retailer
# 3. the product has validations

from django.urls import reverse
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from rest_framework import status
from rest_framework.test import APITestCase

User = get_user_model()

class CreateProductTest(APITestCase):
    def setUp(self):
        self.seller = User.objects.create_user(
            email="seller@example.com",
            full_name="seller",
            role="seller",
            password="strongpassword@123"
        )

        self.customer = User.objects.create_user(
            email="customer@example.com",
            full_name="customer",
            role="customer",
            password="strongpassword@123"
        )

        self.product_data = {
            "name": "Test Product",
            "quantity": 32,
            "price" : 232.24,
            "discount" : 25.50
        }

        self.product_url = reverse('create_product')
        self.login_url = reverse('login')

    def authenticate(self, email, password):
        response:HttpResponse = self.client.post(self.login_url,
                                    {"email":email,
                                     "password":password
                                     },
                                     format="json")
        token = response.data.get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    def test_product_can_be_created_by_seller(self):
        self.authenticate("seller@example.com", "strongpassword@123")
        response = self.client.post(self.product_url, self.product_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_product_can_be_created_by_customer(self):
        self.authenticate("customer@example.com", "strongpassword@123")
        response = self.client.post(self.product_url, self.product_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)