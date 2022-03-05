from django.urls import path
from user import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    # - - - - - - - - - - - - - - - REGISTRATION - - - - - - - - - - - - - - - #

    path('register/', views.register, name='register'),
    path('register_creator/', views.register_creator, name='register_creator'),
    path('login_form/', views.login_form, name='login_form'),

    # - - - - - - - - - - - - - - - USER PROFILE / DASHBOARD - - - - - - - - - - - - - - - #

    path('client/', views.client, name='client'),
    path('creator/', views.creator, name='creator'),

    # - - - - - - - - - - - - - - - CLIENT- - - - - - - - - - - - - - - #

    path('user_update_client/', views.user_update_client, name='user_update_client'),
    path('user_password_client/', views.user_password_client, name='user_password_client'),
    path('user_orders_product/', views.user_orders_product, name='user_orders_product'),
    path('user_orders_product_detail/<int:id>/<int:oid>', views.user_orders_product_detail, name='user_orders_product_detail'),
    path('order_delate_client/<int:pk>', views.order_delate_client, name='order_delate_client'),

    # - - - - - - - - - - - - - - - USER SETTINGS - - - - - - - - - - - - - - - #

    path('logout_form/', views.logout_form, name='logout_form'),
    path('password/', views.user_password, name='user_password'),
    path('update/', views.user_update, name='user_update'),

    # - - - - - - - - - - - - - - - INFORMATION - - - - - - - - - - - - - - - #

    path('information_add/', views.information_add, name='information_add'),
    path('information_update/', views.information_update, name='information_update'),
    path('information_edit/<int:id>', views.information_edit, name='information_edit'),
    path('information_delete/<int:id>', views.information_delete, name='information_delete'),
    path('information_delete_all/', views.information_delete_all, name='information_delete_all'),

    # - - - - - - - - - - - - - - - CATEGORY - - - - - - - - - - - - - - - #

    path('category_add/', views.category_add, name='category_add'),
    path('category_update/', views.category_update, name='category_update'),
    path('category_edit/<int:id>', views.category_edit, name='category_edit'),
    path('category_delete/<int:id>', views.category_delete, name='category_delete'),
    path('category_delete_all/', views.category_delete_all, name='category_delete_all'),

    # - - - - - - - - - - - - - - - PRODUCT - - - - - - - - - - - - - - - #

    path('product_add/', views.product_add, name='product_add'),
    path('product_update/', views.product_update, name='product_update'),
    path('product_edit/<int:id>', views.product_edit, name='product_edit'),
    path('product_delete/<int:id>', views.product_delete, name='product_delete'),
    path('product_delete_all/', views.product_delete_all, name='product_delete_all'),

    # - - - - - - - - - - - - - - - ORDER - - - - - - - - - - - - - - - #

    path('order_all/', views.order_all, name='order_all'),
    path('orders/<int:id>', views.orders, name='orders'),
    path('order_delete/<int:pk>', views.order_delete, name='order_delete'),
    path('order_delete_all/', views.order_delete_all, name='order_delete_all'),

    # - - - - - - - - - - - - - - - DETAIL - - - - - - - - - - - - - - - #

    path('detail_add/', views.detail_add, name='detail_add'),
    path('detail_update/', views.detail_update, name='detail_update'),
    path('detail_edit/<int:id>', views.detail_edit, name='detail_edit'),
    path('detail_delete/<int:id>', views.detail_delete, name='detail_delete'),
    path('detail_delete_all/', views.detail_delete_all, name='detail_delete_all'),

    # - - - - - - - - - - - - - - - NEWS - - - - - - - - - - - - - - - #

    path('news_add/', views.news_add, name='news_add'),
    path('news_update/', views.news_update, name='news_update'),
    path('news_edit/<int:id>', views.news_edit, name='news_edit'),
    path('news_delete/<int:id>', views.news_delete, name='news_delete'),
    path('news_delete_all/', views.news_delete_all, name='news_delete_all'),

    # - - - - - - - - - - - - - - - ABOUT - - - - - - - - - - - - - - - #

    path('about_add/', views.about_add, name='about_add'),
    path('about_update/', views.about_update, name='about_update'),
    path('about_edit/<int:id>', views.about_edit, name='about_edit'),
    path('about_delete/<int:id>', views.about_delete, name='about_delete'),
    path('about_delete_all/', views.about_delete_all, name='about_delete_all'),

    # - - - - - - - - - - - - - - - FAQ - - - - - - - - - - - - - - - #

    path('faq_add/', views.faq_add, name='faq_add'),
    path('faq_update/', views.faq_update, name='faq_update'),
    path('faq_edit/<int:id>', views.faq_edit, name='faq_edit'),
    path('faq_delete/<int:id>', views.faq_delete, name='faq_delete'),
    path('faq_delete_all/', views.faq_delete_all, name='faq_delete_all'),

    # - - - - - - - - - - - - - - - NEWSLETTER - - - - - - - - - - - - - - - #

    path('newsletter_get/', views.newsletter_get, name='newsletter_get'),
    path('newsletter_delete/<int:id>', views.newsletter_delete, name='newsletter_delete'),
    path('newsletter_delete_all/', views.newsletter_delete_all, name='newsletter_delete_all'),

    # - - - - - - - - - - - - - - - CONTACT - - - - - - - - - - - - - - - #

    path('contact_get/', views.contact_get, name='contact_get'),
    path('contact_edit/<int:id>', views.contact_edit, name='contact_edit'),
    path('contact_delete/<int:id>', views.contact_delete, name='contact_delete'),
    path('contact_delete_all/', views.contact_delete_all, name='contact_delete_all'),

    # - - - - - - - - - - - - - - - COMMENT NEWS - - - - - - - - - - - - - - - #

    path('news_comment_get/', views.news_comment_get, name='news_comment_get'),
    path('news_comment_edit/<int:id>', views.news_comment_edit, name='news_comment_edit'),
    path('news_comment_delete/<int:id>', views.news_comment_delete, name='news_comment_delete'),
    path('news_comment_delete_all/', views.news_comment_delete_all, name='news_comment_delete_all'),

    # - - - - - - - - - - - - - - - COMMENT PRODUCT - - - - - - - - - - - - - - - #

    path('product_comment_get/', views.product_comment_get, name='product_comment_get'),
    path('product_comment_edit/<int:id>', views.product_comment_edit, name='product_comment_edit'),
    path('product_comment_delete/<int:id>', views.product_comment_delete, name='product_comment_delete'),
    path('product_comment_delete_all/', views.product_comment_delete_all, name='product_comment_delete_all'),

    # - - - - - - - - - - - - - - - USER - - - - - - - - - - - - - - - #

    path('users_get/', views.users_get, name='users_get'),
    path('user_add_permission/<int:id>', views.user_add_permission, name='user_add_permission'),
    path('users_delete/<int:id>', views.users_delete, name='users_delete'),
    path('users_delete_all/', views.users_delete_all, name='users_delete_all'),

    # - - - - - - - - - - - - - - - PRODUCT GALLERY - - - - - - - - - - - - - - - #

    path('product_gallery/', views.product_gallery, name='product_gallery'),
    path('product_gallery_id/<int:id>', views.product_gallery_id, name='product_gallery_id'),

    # - - - - - - - - - - - - - - - SEARCH - - - - - - - - - - - - - - - #

    path('searched/', views.searched, name='searched'),

    # - - - - - - - - - - - - - - - SLIDER - - - - - - - - - - - - - - - #

    path('slider_add/', views.slider_add, name='slider_add'),
    path('slider_update/', views.slider_update, name='slider_update'),
    path('slider_edit/<int:id>', views.slider_edit, name='slider_edit'),
    path('slider_delete/<int:id>', views.slider_delete, name='slider_delete'),
    path('slider_delete_all/', views.slider_delete_all, name='slider_delete_all'),

    # - - - - - - - - - - - - - - - SLIDER - - - - - - - - - - - - - - - #

    path('add_adversiting/', views.add_adversiting, name='add_adversiting'),
    path('adversiting_update/', views.adversiting_update, name='adversiting_update'),
    path('adversiting_edit/<int:id>', views.adversiting_edit, name='adversiting_edit'),
    path('adversiting_delate/<int:id>', views.adversiting_delate, name='adversiting_delate'),
    path('adversiting_delate_all/', views.adversiting_delate_all, name='adversiting_delate_all'),

    # - - - - - - - - - - - - - - - RESET PASSWORD - - - - - - - - - - - - - - - #

    path('password_reset',
         auth_views.PasswordResetView.as_view(template_name='Reset_password/password_reset_form.html'),
         name='password_reset'),
    path('password_reset_done',
         auth_views.PasswordResetDoneView.as_view(template_name='Reset_password/password_reset_done.html'),
         name='password_reset_done'),
    path('password_reset_confirm/<slug:uidb64>/<slug:token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='Reset_password/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password_reset_complete',
         auth_views.PasswordResetCompleteView.as_view(template_name='Reset_password/password_reset_complete.html'),
         name='password_reset_complete'),

    # - - - - - - - - - - - - - - - BRANDS - - - - - - - - - - - - - - - #

    path('add_brand/', views.add_brand, name='add_brand'),
    path('brand_update/', views.brand_update, name='brand_update'),
    path('brand_edit/<int:id>', views.brand_edit, name='brand_edit'),
    path('brand_delate/<int:id>', views.brand_delate, name='brand_delate'),
    path('brand_delate_all/', views.brand_delate_all, name='brand_delate_all'),

    # - - - - - - - - - - - - - - - BRANDS - - - - - - - - - - - - - - - #

    path('search_dashbourd/', views.search_dashbourd, name='search_dashbourd'),

]
