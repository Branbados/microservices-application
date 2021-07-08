from rest_framework import viewsets

class ProductViewSet(viewsets.ViewSet):
    # /api/products
    def list(self, request):
        ...

    # /api/products
    def create(self, request):
        ...

    # /api/products/<str:id>
    def retrieve(self, request, pk=None):
        ...

    # /api/products/<str:id>
    def update(self, request, pk=None):
        ...

    # /api/products/<str:id>
    def destroy(self, request, pk=None):
        ...