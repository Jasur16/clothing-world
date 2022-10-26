from modeltranslation.translator import register, TranslationOptions
from .models import ProductModel, CategoryModel, ProductTagModel, BarCategoryModel, ColorModel, ShopDetailImageModel


@register(ProductModel)
class ProductmodelTranslationOptions(TranslationOptions):
    fields = ['title', 'short_description', 'long_description', ]


@register(CategoryModel)
class CategoryModelTranslationOptions(TranslationOptions):
    fields = ['name']


@register(ProductTagModel)
class ProductTagModelTranslationOptions(TranslationOptions):
    fields = ['name']


@register(BarCategoryModel)
class BarCategoryModelTranslationOptions(TranslationOptions):
    fields = ['name', 'title']


@register(ColorModel)
class ColorModelTranslationOptions(TranslationOptions):
    fields = ['name']


@register(ShopDetailImageModel)
class ShopDetailTranslationOptions(TranslationOptions):
    fields = ['title']
