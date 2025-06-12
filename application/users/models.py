from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

from .managers import CustomUserManager

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('customer', 'Customer'),
        ('admin', 'Admin/Staff'),
    )
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    def __str__(self):
        return f"{self.email} ({self.role})"


class CustomerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='customer_profile')
    address = models.TextField(blank=True)
    phone_number = models.CharField(max_length=15, blank=True)

class AdminProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='admin_profile')
    department = models.CharField(max_length=100, blank=True)
    access_level = models.IntegerField(default=1)
