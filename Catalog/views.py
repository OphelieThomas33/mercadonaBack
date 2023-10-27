from rest_framework import viewsets
from django.http import HttpResponse
from Catalog.serializers import ProductSerializer, CategorySerializer, DiscountSerializer
from Catalog.models import Product, Category, Discount


# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class DiscountViewSet(viewsets.ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.prefetch_related('category').select_related('discount').all()
    serializer_class = ProductSerializer

#
# def post(request, *args, **kwargs):
#     label = request.data['label']
#     description = request.data['description']
#     price = request.data['price']
#     image = request.data['image']
#     category = request.data['category']
#     discount = request.data['discount']
#     Product.objects.create(label=label,
#                            description=description,
#                            price=price,
#                            image=image,
#                            category=category,
#                            discount=discount
#                            )
#     return HttpResponse({'Message': 'Product created'}, status=200)
