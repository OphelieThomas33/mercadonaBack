from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Catalog.views import ProductViewSet, CategoryViewSet, DiscountViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, 'product')
router.register(r'categories', CategoryViewSet, 'category')
router.register(r'discounts', DiscountViewSet, 'discount')

urlpatterns = [
    path("", include(router.urls)),
]
