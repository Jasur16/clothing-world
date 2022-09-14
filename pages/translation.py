from modeltranslation.translator import register, TranslationOptions
from .models import AboutModel, MenBannerModel


@register(AboutModel)
class AboutModelTranslationOptions(TranslationOptions):
    fields = ['our_story', 'our_mission']


@register(MenBannerModel)
class MenBannerModelTranslationOptions(TranslationOptions):
    fields = ['collections', 'title', ]
