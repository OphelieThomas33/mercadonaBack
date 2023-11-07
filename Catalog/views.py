from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from Catalog.serializers import ProductSerializer, CategorySerializer, DiscountSerializer
from Catalog.models import Product, Category, Discount


# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects\
        .select_related()\
        .prefetch_related('products')\
        .all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class DiscountViewSet(viewsets.ModelViewSet):
    queryset = Discount.objects.select_related().all()
    serializer_class = DiscountSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects\
        .prefetch_related('category')\
        .select_related('discount')\
        .all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
