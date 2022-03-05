from modeltranslation.translator import register, TranslationOptions
from blog.models import Blog


@register(Blog)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)

