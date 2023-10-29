from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from Catalog.serializers import ProductSerializer, CategorySerializer, DiscountSerializer
from Catalog.models import Product, Category, Discount


# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects\
        .select_related()\
        .prefetch_related('products')\
        .all()
    serializer_class = CategorySerializer


class DiscountViewSet(viewsets.ModelViewSet):
    queryset = Discount.objects.select_related().all()
    serializer_class = DiscountSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects\
        .prefetch_related('category')\
        .select_related('discount')\
        .all()
    serializer_class = ProductSerializer

    # @action(detail=False)
    # def discounted_products(self, request):
    #     discounted_products = self.queryset.filter(category__products__discount__isnull=False)
    #     serializer = self.get_serializer(discounted_products, many=True)
    #     return Response(serializer.data)
