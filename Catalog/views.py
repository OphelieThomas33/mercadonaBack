from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from Catalog.serializers import ProductSerializer, CategorySerializer, DiscountSerializer
from Catalog.models import Product, Category, Discount


# setting API policy on category view set
class CategoryViewSet(viewsets.ModelViewSet):
    # display all categories by showing associated products and categories
    queryset = Category.objects\
        .select_related()\
        .prefetch_related('products')\
        .all()
    serializer_class = CategorySerializer
    # read-only for anonymous users and editable for authenticated user
    permission_classes = (IsAuthenticatedOrReadOnly,)


# setting API policy on discount view set
class DiscountViewSet(viewsets.ModelViewSet):
    # display all discounts
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
    # read-only for anonymous users and editable for authenticated user
    permission_classes = (IsAuthenticatedOrReadOnly,)


# setting API policy on product view set
class ProductViewSet(viewsets.ModelViewSet):
    # display all products by showing associated discount and categories
    queryset = Product.objects\
        .prefetch_related('category')\
        .select_related('discount')\
        .all()
    serializer_class = ProductSerializer
    # read-only for anonymous users and editable for authenticated user
    permission_classes = (IsAuthenticatedOrReadOnly,)
