from django.core.exceptions import ValidationError
from django.db import models

from core.models import AuditDetailsModel

class Product(AuditDetailsModel):
    name = models.CharField(max_length=255)
    quantity = models.FloatField(max_length=4)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    discount = models.DecimalField(max_digits=4, decimal_places=2)

    def clean(self):
        if not (0<=self.discount<=100):
            return ValidationError({"discount": "Discount must be between 0 and 100"})
        
    @property
    def discounted_price(self):
        return round(self.price*(1-self.discount/100),2)