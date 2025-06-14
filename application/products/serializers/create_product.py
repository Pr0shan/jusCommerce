from rest_framework.serializers import ModelSerializer, SerializerMethodField, ValidationError
from products.models import Product

class CreateProductSerializer(ModelSerializer):
    discounted_price = SerializerMethodField(read_only=True)

    class Meta:
        model=Product
        fields=['id', 'name', 'quantity', 'price', 'discount', 'discounted_price', 'created_on', 'created_by']
        read_only_fields=['created_on', 'created_by', 'discounted_price']

    def get_discounted_price(self, obj):
        return obj.discounted_price
    
    def validate_discount(self, value):
        if not (0<=value<=100):
            raise ValidationError("Discount must be between 0 and 100")
        return value