"""User models admin."""

#Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

#Models
from users.models import User, Profile

class ProfileInline(admin.TabularInline):
    """Inline profile"""
    model = Profile
    fk_name = "user"

class CustomUserAdmin(UserAdmin):
    """User model admin."""
    inlines = [
        ProfileInline,
    ]

    list_display = ('email','username', 'first_name','last_name', 'is_staff', 'is_active', 'is_verified')
    list_filter = ('is_active', 'is_staff', 'created', 'modified')
    list_editable = ('is_verified',)

admin.site.register(User, CustomUserAdmin)