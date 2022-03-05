from django import forms
from home.models import ContactMessage, NewsLatter, Wishlist


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ('name', 'surname', 'email', 'subject', 'message',)


class NewsLatterForm(forms.ModelForm):
    class Meta:
        model = NewsLatter
        fields = ('email',)


class WishlistForm(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = ['quantity', ]
