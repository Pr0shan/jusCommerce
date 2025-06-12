from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    """
    Custom user manager to require email for account creation
    """
    def create_user(self, email, password, role='customer', **extra_fields):
        if not email:
            raise ValueError("Email must be provided")
        email = self.normalize_email(email)
        user = self.model(email=email, role=role, password=password, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, role='admin', **extra_fields)
    