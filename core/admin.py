from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Employee, User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "username", "password1", "password2"),
            },
        ),
    )

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass