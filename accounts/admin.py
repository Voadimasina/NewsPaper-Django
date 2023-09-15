from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        'email',
        'username',
        'sigle',
        'age',
        'is_staff',
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {'fields':('sigle','age',)}),)
    add_fieldsets = UserAdmin.fieldsets + ((None, {'fields':('sigle','age',)}),)

admin.site.register(CustomUser, CustomUserAdmin)