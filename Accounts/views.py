from rest_framework import viewsets


from Accounts.models import CustomUser, Employee
from Accounts.serializers import CustomUserSerializer, EmployeeSerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class EmployeeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


