from django.contrib import admin
from .models import OrderHistoryModel


@admin.register(OrderHistoryModel)
class ShopHistoryModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name']
    list_display_links = ['user', 'first_name', 'last_name']
    # readonly_fields = ['user', 'products', 'first_name', 'last_name', 'phone', 'city', 'address', 'gmail', 'comment']
