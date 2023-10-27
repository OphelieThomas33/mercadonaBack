from datetime import date
from django.db import models
from django.contrib.auth.models import AbstractUser
import Stores.models


# Create your models here.
class CustomUser(AbstractUser):
    birth_date = models.DateField(default=date.today)

    class Meta:
        db_table = "accounts_custom_user"


class Customer(CustomUser):

    class Meta:
        db_table = "accounts_customer"
        verbose_name = "customer"
        verbose_name_plural = "customers"


class Employee(CustomUser):
    company = models.ForeignKey(Stores.models.Company, on_delete=models.CASCADE)

    class Meta:
        db_table = "accounts_employee"
        verbose_name = "employee"
        verbose_name_plural = "employees"
