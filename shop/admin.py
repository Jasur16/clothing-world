from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import ProductModel, ProductTagModel, CategoryModel, BarCategoryModel, SizeModel, ColorModel, \
    ProductDetailImageModel
from .forms import ColorModelAdminForms


@admin.register(ProductDetailImageModel)
class ProductDetailImageModelAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_display_links = ['title']
    list_filter = ['created_at']


@admin.register(ProductTagModel)
class ProductTagModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']


@admin.register(SizeModel)
class SizeModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']


@admin.register(ColorModel)
class ColorModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'color']
    list_display_links = ['name', 'code']
    search_fields = ['name', 'code']
    form = ColorModelAdminForms

    def color(self, obj):
        free_space = '&nbsp'
        return mark_safe(f"<div style='width: 150px; background-color: {obj.code}'>{free_space}</div>")


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']


@admin.register(BarCategoryModel)
class BarCategoryModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'title']
    list_display_links = ['name', 'title']
    search_fields = ['name', 'title']


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'discount', 'real_price', 'created_at']
    list_display_links = ['title', 'price', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'price']
    autocomplete_fields = ['category', 'tags', 'sizes', 'colors']
    readonly_fields = ['real_price']
