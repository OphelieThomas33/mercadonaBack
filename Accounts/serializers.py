from django.contrib.auth.models import Group
from rest_framework import serializers

from Accounts.models import Employee, CustomUser


# Information on groups to send to the API
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


# Information on users to send to the API
class CustomUserSerializer(serializers.ModelSerializer):
    # call to a groupSerializer to allow the display of groups
    groups = GroupSerializer(many=True)

    class Meta:
        model = CustomUser
        fields = ('id',
                  'first_name',
                  'last_name',
                  'groups')


# Information on employees to send to the API
class EmployeeSerializer(serializers.ModelSerializer):
    # call to a groupSerializer to allow the display of groups
    groups = GroupSerializer(many=True)

    class Meta:
        model = Employee
        fields = ('id',
                  'first_name',
                  'last_name',
                  'groups')