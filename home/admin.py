from django.contrib import admin
from home.models import ContactMessage, Aboutus, Faq, Informations, Slider
from user.models import Brands


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'email', 'message', 'creat_at', ]
    readonly_fields = ('name', 'subject', 'email', 'message', 'creat_at',)
    list_filter = ['status']


class AboutusAdmin(admin.ModelAdmin):
    list_display = ['title', ]


class InfoAdmin(admin.ModelAdmin):
    list_display = ['title', 'country', 'city', 'address', 'phone', 'email', 'telegram', 'instagram',
                    'facebook', 'twitter', 'description', 'create_at', ]
    list_filter = ['status']


class FaqAdmin(admin.ModelAdmin):
    list_display = ['ordernumber', 'question', 'answer', 'create_at', ]
    list_filter = ['status']


class SliderAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'image', 'create_at', ]
    list_filter = ['status']


class BrandAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'create_at', ]
    list_filter = ['status']


admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(Aboutus, AboutusAdmin)
admin.site.register(Informations, InfoAdmin)
admin.site.register(Faq, FaqAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(Brands, BrandAdmin)
