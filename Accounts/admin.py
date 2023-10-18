from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
# Register your models here.
from .models import Customer, Employee, CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "username"]


# Register your models here.
admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(CustomUser, CustomUserAdmin)

