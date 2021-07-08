from rest_framework import viewsets, status
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response

class ProductViewSet(viewsets.ViewSet):
    # /api/products
    def list(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    # /api/products
    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # /api/products/<str:id>
    def retrieve(self, request, pk=None):
        ...

    # /api/products/<str:id>
    def update(self, request, pk=None):
        ...

    # /api/products/<str:id>
    def destroy(self, request, pk=None):
        ...