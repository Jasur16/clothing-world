from django.contrib import admin
from .models import ContactModel, MenBannerModel, WomenBannerModel, AboutModel


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at']
    list_display_links = ['name', 'email']
    search_fields = ['name', 'email', 'message']
    list_filter = ['created_at']


@admin.register(MenBannerModel)
class MenBannerModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'collections', 'is_active']
    list_display_links = ['title', 'collections']
    search_fields = ['title', 'collections']
    list_filter = ['created_at']


@admin.register(WomenBannerModel)
class WomenBannerModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'collections', 'is_active']
    list_display_links = ['title', 'collections']
    search_fields = ['title', 'collections']
    list_filter = ['created_at']


@admin.register(AboutModel)
class AboutModelAdmin(admin.ModelAdmin):
    list_display = ['our_story', 'our_mission']
    list_display_links = ['our_story', 'our_mission']
    list_filter = ['created_at']

