from modeltranslation.translator import register, TranslationOptions
from home.models import Informations, Aboutus, Faq, Slider, Adversiting


@register(Informations)
class InformationsTranslationOptions(TranslationOptions):
    fields = ('title', 'address', 'description',)


@register(Aboutus)
class InformationsTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


@register(Faq)
class InformationsTranslationOptions(TranslationOptions):
    fields = ('question', 'answer',)


@register(Slider)
class SliderTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)

@register(Adversiting)
class AdversitingTranslationOptions(TranslationOptions):
    fields = ('title',)
