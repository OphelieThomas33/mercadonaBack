from datetime import date
from django.db import models
from django.contrib.auth.models import AbstractUser
import Stores.models


# custom user with addition of the date of birth field
# this user could be an employee or a consumer
class CustomUser(AbstractUser):
    birth_date = models.DateField(default=date.today)

    class Meta:
        db_table = "accounts_custom_user"
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"


# customer table (useful for the evolution of the site)
class Customer(CustomUser):

    class Meta:
        db_table = "accounts_customer"
        verbose_name = "Client"
        verbose_name_plural = "Clients"


# employee table
class Employee(CustomUser):
    company = models.ForeignKey(Stores.models.Company, on_delete=models.CASCADE)

    class Meta:
        db_table = "accounts_employee"
        verbose_name = "Employé"
        verbose_name_plural = "Employés"
