from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly

from Accounts.models import CustomUser, Employee
from Accounts.serializers import CustomUserSerializer, EmployeeSerializer


# setting API policy on customUser view set
class CustomUserViewSet(viewsets.ModelViewSet):
    # display all users
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    # read-only for anonymous users and editable for authenticated user (group=admin)
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)


# setting API policy on employee view set
class EmployeeViewSet(viewsets.ReadOnlyModelViewSet):
    # display all employees
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    # read-only for anonymous users and editable for authenticated user (group=admin)
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)


