# TODO
# create view for product

from products.serializers import CreateProductSerializer

from rest_framework.generics import CreateAPIView


class CreateProduct(CreateAPIView):
    serializer_class = CreateProductSerializer

    def perform_create(self, serializer:CreateProductSerializer):
        user = None
        serializer.save(created_by=user, updated_by=user)
        return super().perform_create(serializer)
    
