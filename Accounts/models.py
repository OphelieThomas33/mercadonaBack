from datetime import date
from django.db import models
from django.contrib.auth.models import AbstractUser
import Stores.models


# Create your models here.
class CustomUser(AbstractUser):
    birth_date = models.DateField(default=date.today)


class Customer(CustomUser):

    class Meta:
        verbose_name = "customer"
        verbose_name_plural = "customers"


class Employee(CustomUser):
    company = models.ForeignKey(Stores.models.Company, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "employee"
        verbose_name_plural = "employees"
