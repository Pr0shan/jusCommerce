from django.urls import path
from .views import create_product_view

urlpatterns = [
    path('', create_product_view, name='create_product')
]
