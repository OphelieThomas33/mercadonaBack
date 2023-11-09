from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


# form to connect a CustomUser on django admin panel
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email")


# form to modify a CustomUser on django admin panel
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email")
