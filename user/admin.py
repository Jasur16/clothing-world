from django.contrib import admin
from .models import ProfileModel


@admin.register(ProfileModel)
class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'first_name', 'last_name', 'phone', 'email', 'city', 'created_at']
    readonly_fields = ['first_name', 'last_name', 'phone', 'email', 'address', 'city', 'user']
