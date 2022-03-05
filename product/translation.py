from modeltranslation.translator import register, TranslationOptions
from product.models import Category, Product, Images


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


