from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product_detail/<int:id>/<slug:slug>', views.product_detail, name='product_detail'),
    path('category_product/<int:id>/<slug:slug>', views.category_product, name='category_product'),
    path('contactus/', views.contactus, name='contactus'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('faq/', views.faq, name='faq'),
    path('search/', views.search, name='search'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('footer/', views.footer, name='footer'),
    path('header/', views.header, name='header'),
    path('newsLatter/', views.newsLatter, name='newsLatter'),
]
