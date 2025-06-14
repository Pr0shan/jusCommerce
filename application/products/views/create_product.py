# TODO
# create view for product

# serializers
from products.serializers import CreateProductSerializer

# api views
from rest_framework.generics import CreateAPIView

# permission_classes
from core.permissions import IsSeller
from rest_framework.permissions import IsAuthenticated

class CreateProduct(CreateAPIView):
    serializer_class = CreateProductSerializer
    permission_classes = [IsAuthenticated, IsSeller]
    
    def perform_create(self, serializer:CreateProductSerializer):
        user = None
        serializer.save(created_by=user, updated_by=user)
        return super().perform_create(serializer)
    
