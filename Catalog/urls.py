from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Catalog.views import ProductViewSet, CategoryViewSet, DiscountViewSet, ReadProductViewSet

# definition of routes based on views
router = DefaultRouter()
router.register(r'products', ProductViewSet, 'product')
router.register(r'categories', CategoryViewSet, 'category')
router.register(r'discounts', DiscountViewSet, 'discount')
router.register(r'products-list', ReadProductViewSet, 'product-list')

# creating routes for API
urlpatterns = [
    path("", include(router.urls)),
]
