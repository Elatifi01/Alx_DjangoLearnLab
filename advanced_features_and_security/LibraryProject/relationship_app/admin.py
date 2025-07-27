from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, UserProfile

class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # Add your custom fields to admin fieldsets (edit form)
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

    # Add custom fields to admin add user form
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

    # Columns to display in the user list in admin
    list_display = ['username', 'email', 'date_of_birth', 'is_staff']

# Register your models with the admin site
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserProfile)