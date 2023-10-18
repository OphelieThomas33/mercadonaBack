from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Catalog.views import ProductViewSet, CategoryViewSet, DiscountViewSet


router = DefaultRouter()
router.register('products', ProductViewSet, 'product')
router.register('categories', CategoryViewSet, 'category')
router.register('discounts', DiscountViewSet, 'discount')


urlpatterns = [
    path('', include(router.urls))
]
