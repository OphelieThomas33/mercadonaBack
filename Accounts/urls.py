from django.urls import path, include
from rest_framework.routers import DefaultRouter

from Accounts.views import EmployeeViewSet

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet, 'employee')

urlpatterns = [
    path("", include(router.urls)),
]
