from modeltranslation.translator import register, TranslationOptions
from .models import PostModel


@register(PostModel)
class PostmodelTranslationOptions(TranslationOptions):
    fields = ['title', 'body']
