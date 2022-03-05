from modeltranslation.translator import register, TranslationOptions
from user.models import Brands


@register(Brands)
class BrandsTranslationOptions(TranslationOptions):
    fields = ('title',)



