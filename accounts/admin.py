from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "name",
        "phone_number",
        "is_approved",
        "is_admin",
    ]

    # Define fieldsets for the change view
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('name', 'phone_number', 'is_approved', 'is_admin')}),
    )

    # Update add_fieldsets to include 'name', 'phone_number', 'is_approved', and 'is_admin'
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "name",
                    "phone_number",
                    "is_approved",
                    "is_admin",
                    "password1",
                    "password2",
                ),
            },
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)