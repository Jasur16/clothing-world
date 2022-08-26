from modeltranslation.translator import register, TranslationOptions
from .models import PostModel, CommentModel


@register(PostModel)
class PostmodelTranslationOptions(TranslationOptions):
    fields = ['title', 'body']
