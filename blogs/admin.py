from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin


@admin.register(PostTagModel)
class TagModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    list_filter = ['created_at']
    search_fields = ['name']


@admin.register(PostModel)
class PostModelAdmin(TranslationAdmin):
    list_display = ['title', 'created_at']
    list_display_links = ['title']
    list_filter = ['created_at']
    autocomplete_fields = ['auther', 'tag']

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(CommentModel)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'post']
    list_display_links = ['name', 'email', 'phone']
    search_fields = ['name']
    readonly_fields = ['comment', 'name', 'email', 'phone']


@admin.register(AutherModel)
class AutherModelAdmin(admin.ModelAdmin):
    list_display = ['full_name']
    list_display_links = ['full_name']
    search_fields = ['full_name']
