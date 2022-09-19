from django.contrib import admin

from .models import OrderHistoryModel


@admin.register(OrderHistoryModel)
class ShopHistoryModelAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    list_display_links = ['first_name', 'last_name']
