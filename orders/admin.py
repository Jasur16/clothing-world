from django.contrib import admin

from .models import ShopHistoryModel


@admin.register(ShopHistoryModel)
class ShopHistoryModelAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    list_display_links = ['first_name', 'last_name']
