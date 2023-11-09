from django.urls import path, include
from rest_framework.routers import DefaultRouter

from Accounts.views import EmployeeViewSet

# definition of routes based on views
router = DefaultRouter()
router.register(r'employees', EmployeeViewSet, 'employee')

# creating routes for API
urlpatterns = [
    path("", include(router.urls)),
]
