from django.contrib.auth.models import Group
from rest_framework import serializers

from Accounts.models import Employee, CustomUser


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class CustomUserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True)

    class Meta:
        model = CustomUser
        fields = ('id',
                  'first_name',
                  'last_name',
                  'groups')


class EmployeeSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True)

    class Meta:
        model = Employee
        fields = ('id',
                  'first_name',
                  'last_name',
                  'groups')