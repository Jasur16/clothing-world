from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import ProductModel, ProductTagModel, CategoryModel, BarCategoryModel, SizeModel, ColorModel, \
    ProductDetailImageModel, ShopHistoryModel
from .forms import ColorModelAdminForms
from modeltranslation.admin import TranslationAdmin



@admin.register(ShopHistoryModel)
class ShopHistoryModelAdmin(admin.ModelAdmin):
    list_display = ['full_name']
    list_display_links = ['full_name']


@admin.register(ProductDetailImageModel)
class ProductDetailImageModelAdmin(TranslationAdmin):
    list_display = ['title']
    list_display_links = ['title']
    list_filter = ['created_at']

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(ProductTagModel)
class ProductTagModelAdmin(TranslationAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(SizeModel)
class SizeModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']


@admin.register(ColorModel)
class ColorModelAdmin(TranslationAdmin):
    list_display = ['name', 'code', 'color']
    list_display_links = ['name', 'code']
    search_fields = ['name', 'code']
    form = ColorModelAdminForms

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

    def color(self, obj):
        free_space = '&nbsp'
        return mark_safe(f"<div style='width: 150px; background-color: {obj.code}'>{free_space}</div>")


@admin.register(CategoryModel)
class CategoryModelAdmin(TranslationAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(BarCategoryModel)
class BarCategoryModelAdmin(TranslationAdmin):
    list_display = ['name', 'title']
    list_display_links = ['name', 'title']
    search_fields = ['name', 'title']

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(ProductModel)
class ProductModelAdmin(TranslationAdmin):
    list_display = ['title', 'price', 'discount', 'real_price', 'created_at']
    list_display_links = ['title', 'price', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'price']
    autocomplete_fields = ['category', 'tags', 'sizes', 'colors']
    readonly_fields = ['real_price']

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
