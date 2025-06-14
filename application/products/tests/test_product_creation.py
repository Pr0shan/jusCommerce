# TODO: Test
# 1. the product can be created
# 2. the product can only be created by retailer
# 3. the product has validations

from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APITestCase

User = get_user_model()

class CreateProductTest(APITestCase):
    def test_product_can_be_created(self):
        url = reverse('create_product')
        data = {
            "name": "Test Product",
            "quantity": 32,
            "price" : 232.24,
            "discount" : 25.50
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)