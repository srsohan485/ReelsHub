from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'is_active', 'date_joined']
    search_fields = ['username', 'email']
    list_filter = ['is_active', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        ('Extra Info', {'fields': ('bio', 'profile_picture', 'followers')}),
    )