from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from home.models import Informations, Aboutus, Faq, ContactMessage, Slider, Adversiting
from blog.models import Blog, Comment_blog
from order.models import OrderProduct
from product.models import Product, Category, Images, Comment
from user.models import Client, Creator, Brands


# - - - - - - - - - - - - - - - REGISTRATION - - - - - - - - - - - - - - - #

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=255, label='Username')
    email = forms.CharField(max_length=255, label='Email')
    first_name = forms.CharField(max_length=255, label='Firstname')
    last_name = forms.CharField(max_length=255, label='Lastname')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class UserClientUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class ProfileClinetUpdateForms(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['phone', 'address', 'city', 'country', 'image', 'description', ]


class ProfileCreatorUpdateForm(forms.ModelForm):
    class Meta:
        model = Creator
        fields = ['phone', 'address', 'city', 'country', 'image', ]


# - - - - - - - - - - - - - - - INFORMATIONS - - - - - - - - - - - - - - - #

class AddInformationForm(forms.ModelForm):
    class Meta:
        model = Informations
        fields = ['title_uz', 'title_en', 'title_ru', 'country', 'city', 'address_en', 'address_ru', 'address_uz',
                  'phone', 'email',  'telegram', 'instagram', 'facebook', 'twitter', 'status', 'description_uz',
                  'description_en', 'description_ru', 'location', 'logo', 'icon', ]


class EditInformationForm(forms.ModelForm):
    class Meta:
        model = Informations
        fields = ['title_uz', 'title_en', 'title_ru', 'country', 'city', 'address_en', 'address_ru', 'address_uz',
                  'phone', 'email', 'telegram', 'instagram', 'facebook', 'twitter', 'status', 'description_uz',
                  'description_en', 'description_ru', 'location', 'logo', 'icon', ]


# - - - - - - - - - - - - - - - CATEGORY - - - - - - - - - - - - - - - #

class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title_uz', 'title_en', 'title_ru', 'description_uz', 'description_en', 'description_ru', 'image',
                  'slug', 'status']


class EditCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title_uz', 'title_en', 'title_ru', 'description_uz', 'description_en', 'description_ru', 'image',
                  'slug', 'status']


# - - - - - - - - - - - - - - - PRODUCT - - - - - - - - - - - - - - - #

class AddProductsForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'title_en', 'title_ru', 'title_uz', 'old_price', 'sell_price', 'image', 'slug',
                  'status', 'description_en', 'description_ru', 'description_uz']


class EditProductsForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'title_en', 'title_ru', 'title_uz', 'old_price', 'sell_price', 'image', 'slug',
                  'status', 'description_en', 'description_ru', 'description_uz']


# - - - - - - - - - - - - - - - ORDER - - - - - - - - - - - - - - - #

class EditOrderProductForm(forms.ModelForm):
    class Meta:
        model = OrderProduct
        fields = ['status']


# - - - - - - - - - - - - - - - DETAIL - - - - - - - - - - - - - - - #

class AppandDetailsForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ['product', 'image', 'collor', 'size', ]


class EditDetailsForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ['product', 'image', 'collor', 'size', ]


# - - - - - - - - - - - - - - - NEWS - - - - - - - - - - - - - - - #

class AppandNewsForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title_uz', 'title_en', 'title_ru', 'image', 'status', 'description_uz', 'description_en',
                  'description_ru', ]


class EditNewsForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title_uz', 'title_en', 'title_ru', 'image', 'status', 'description_uz', 'description_en',
                  'description_ru', ]


# - - - - - - - - - - - - - - - ABOUT - - - - - - - - - - - - - - - #

class AppandAboutForm(forms.ModelForm):
    class Meta:
        model = Aboutus
        fields = ['title_uz', 'title_en', 'title_ru', 'image', 'status', 'description_uz', 'description_en',
                  'description_ru', ]


class EditAboutForm(forms.ModelForm):
    class Meta:
        model = Aboutus
        fields = ['title_uz', 'title_en', 'title_ru', 'image', 'status', 'description_uz', 'description_en',
                  'description_ru', ]


# - - - - - - - - - - - - - - - FAQ - - - - - - - - - - - - - - - #

class AppandFAQSForm(forms.ModelForm):
    class Meta:
        model = Faq
        fields = ['ordernumber', 'question_en', 'question_ru', 'question_uz', 'status', 'answer_en', 'answer_ru',
                  'answer_uz']


class EditFAQSForm(forms.ModelForm):
    class Meta:
        model = Faq
        fields = ['ordernumber', 'question_en', 'question_ru', 'question_uz', 'status', 'answer_en', 'answer_ru',
                  'answer_uz']


# - - - - - - - - - - - - - - - CONTACT - - - - - - - - - - - - - - - #

class EditContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['status']


# - - - - - - - - - - - - - - - COMMENT NEWS - - - - - - - - - - - - - - - #

class EditNewsCommentForm(forms.ModelForm):
    class Meta:
        model = Comment_blog
        fields = ['status']


# - - - - - - - - - - - - - - - COMMENT PRODUCT - - - - - - - - - - - - - - - #

class EditProductCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['status']


# - - - - - - - - - - - - - - - USER - - - - - - - - - - - - - - - #

class UserPermissonForm(forms.ModelForm):
    class Meta:
        model = Creator
        fields = ['user', 'image']


# - - - - - - - - - - - - - - - SLIDER - - - - - - - - - - - - - - - #

class AppandSliderForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = ['title_uz', 'title_en', 'title_ru', 'image', 'status', 'description_uz', 'description_en',
                  'description_ru', ]


class EditSliderForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = ['title_uz', 'title_en', 'title_ru', 'image', 'status', 'description_uz', 'description_en',
                  'description_ru', ]


# - - - - - - - - - - - - - - - ADVERSITING - - - - - - - - - - - - - - - #

class AppandAversitingForm(forms.ModelForm):
    class Meta:
        model = Adversiting
        fields = ['title_uz', 'title_en', 'title_ru', 'image', 'status', ]


class EditAdversitingForm(forms.ModelForm):
    class Meta:
        model = Adversiting
        fields = ['title_uz', 'title_en', 'title_ru', 'image', 'status', ]


# - - - - - - - - - - - - - - - brand - - - - - - - - - - - - - - - #

class AppandBrandForm(forms.ModelForm):
    class Meta:
        model = Brands
        fields = ['title_uz', 'title_en', 'title_ru', 'image', 'status', ]


class EditBrandForm(forms.ModelForm):
    class Meta:
        model = Brands
        fields = ['title_uz', 'title_en', 'title_ru', 'image', 'status', ]
