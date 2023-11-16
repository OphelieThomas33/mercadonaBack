from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
# Register your models here.
from .models import Customer, Employee, CustomUser


# connection to the django administration panel using username and email
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "username"]


# models to display in django admin panel
admin.site.register(Customer)
admin.site.register(CustomUser, CustomUserAdmin)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    # employee display fields
    list_display = (
        'first_name',
        'last_name',
        'email',
        'get_groups'
    )

    # get groups list by employee
    @admin.display(description="Groupes")
    def get_groups(self, obj):
        return "\n".join([g.name for g in obj.groups.all()])
