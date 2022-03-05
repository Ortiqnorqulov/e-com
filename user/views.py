from django.contrib.auth.forms import PasswordChangeForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.utils import translation
from home.models import ContactMessage, Informations, Slider, NewsLatter, Faq, Aboutus, Adversiting
from blog.models import Comment_blog, Blog
from order.models import Order, OrderProduct, ShopCart
from product.models import Category, Product, Images, Comment
from user.forms import SignUpForm, UserUpdateForm, AddProductsForm, EditProductsForm, \
    EditCategoryForm, AddCategoryForm, AddInformationForm, EditInformationForm, EditOrderProductForm, EditSliderForm, \
    AppandSliderForm, UserPermissonForm, EditContactForm, EditFAQSForm, \
    AppandFAQSForm, EditAboutForm, AppandAboutForm, EditNewsForm, AppandNewsForm, EditDetailsForm, \
    AppandDetailsForm, EditProductCommentForm, EditNewsCommentForm, ProfileCreatorUpdateForm, UserClientUpdateForm, \
    ProfileClinetUpdateForms, AppandAversitingForm, EditAdversitingForm, EditBrandForm, AppandBrandForm
from user.models import Client, Creator, Brands
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# - - - - - - - - - - - - - - - REGISTRATION - - - - - - - - - - - - - - - #


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            current_user = request.user
            data = Client()
            data.user_id = current_user.id
            data.image = "images/users/user.png"
            data.save()
            messages.success(request, 'Your account has been created!')
            return redirect('home')
        else:
            messages.warning(request, form.errors)
            return redirect('home')
    form = SignUpForm()
    context = {
        'form': form,
    }
    return render(request, 'Authenticate/register.html', context)


# - - - - - - - - - - - - - - - LOGIN - - - - - - - - - - - - - - - #

def login_form(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            try:
                Creator.objects.get(user_id=request.user.id)
                return redirect('creator')
            except:
                try:
                    Client.objects.get(user_id=request.user.id)
                    return redirect('client')
                except:
                    return redirect('login_form')
        else:
            messages.warning(request, "Login Error! User name or Password is incorrect")
            return redirect('login_form')

    return render(request, 'Authenticate/login.html')


# - - - - - - - - - - - - - - - CREATOR / ADMIN - - - - - - - - - - - - - - - #

@login_required(login_url='login_form')
def creator(request):
    try:
        creator = Creator.objects.get(user=request.user)
    except:
        messages.warning(request, 'Error Try Again Later')
        return redirect('login_form')
    category = Category.objects.all()
    product = Product.objects.all()
    client = Client.objects.all()
    contact = ContactMessage.objects.all()
    order = Order.objects.all()
    order_product = OrderProduct.objects.all()
    order_product_count = order_product.count()
    category_count = category.count()
    product_count = product.count()
    client_count = client.count()
    contact_count = contact.count()
    context = {
        'client': client,
        'creator': creator,
        'category': category,
        'product': product,
        'contact': contact,
        'order': order,
        'order_product': order_product,
        'category_count': category_count,
        'product_count': product_count,
        'client_count': client_count,
        'contact_count': contact_count,
        'order_product_count': order_product_count,
    }
    return render(request, 'Creator/creator.html', context)


@login_required(login_url='login_form')
def register_creator(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            current_user = request.user
            data = Creator()
            data.user_id = current_user.id
            data.image = "images/users/user.png"
            data.save()
            messages.success(request, 'Your account has been created!')
            return redirect('user_update')
        else:
            messages.warning(request, form.errors)
            return redirect('register_creator')
    form = SignUpForm()
    context = {
        'form': form,
    }
    return render(request, 'Authenticate/register_creator.html', context)


# - - - - - - - - - - - - - - - Client - - - - - - - - - - - - - - - #

def user_update_client(request):
    if request.method == 'POST':
        user_form = UserClientUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileClinetUpdateForms(request.POST, request.FILES, instance=request.user.client)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated')
            return redirect('client')
    else:
        user_form = UserClientUpdateForm(instance=request.user)
        profile_form = ProfileClinetUpdateForms(instance=request.user.client)
        client = Client.objects.get(user=request.user)
        brands = Brands.objects.filter(status='True').order_by('?')
        context = {
            'user_form': user_form,
            'profile_form': profile_form,
            'client': client,
            'brands': brands,
        }
        return render(request, 'Client/user_update_client.html', context)


def user_password_client(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your profile password successfully updated')
            return redirect('client')
        else:
            messages.error(request, 'Eror password')
            return redirect('user_password_client')
    else:
        form = PasswordChangeForm(request.user)
        client = Client.objects.get(user=request.user)
        brands = Brands.objects.filter(status='True').order_by('?')
        context = {
            'form': form,
            'client': client,
            'brands': brands,
        }
        return render(request, 'Client/user_password_client.html', context)


def user_orders_product(request):
    current_user = request.user
    client = Client.objects.get(user=request.user)
    order_product = Order.objects.filter(user_id=current_user.id)
    shopcart_ = ShopCart.objects.filter(user_id=client)
    brands = Brands.objects.filter(status='True').order_by('?')
    context = {
        'shopcart_': shopcart_,
        'order_product': order_product,
        'client': client,
        'brands': brands,
    }
    return render(request, 'Client/page_order_detail.html', context)


def order_delate_client(request, pk):
    current_user = request.user
    orderproduct = OrderProduct.objects.filter(id=pk, user_id=current_user.id)
    order = Order.objects.get(id=pk, user_id=current_user.id)
    orderproduct.delete()
    order.delete()
    return redirect('user_orders_product')


@login_required(login_url='login_form')
def user_orders_product_detail(request, id, oid):
    current_user = request.user
    order = Order.objects.get(user_id=current_user.id, id=oid)
    orderitem = OrderProduct.objects.filter(id=id, user_id=current_user.id)
    client = Client.objects.get(user=request.user)
    context = {
        'orderitem': orderitem,
        'client': client,
        'order': order,
    }
    return render(request, 'Client/page_order_detail.html', context)


# - - - - - - - - - - - - - - - USER PROFILE - - - - - - - - - - - - - - - #

@login_required(login_url='login_form')
def client(request):
    try:
        client = Client.objects.get(user=request.user)
    except:
        messages.warning(request, 'Error Try Again Later')
        return redirect('login_form')

    if request.method == 'POST':
        user_form = UserClientUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileClinetUpdateForms(request.POST, request.FILES, instance=request.user.client)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated')
            return redirect('client')
    else:
        user_form = UserClientUpdateForm(instance=request.user)
        profile_form = ProfileClinetUpdateForms(instance=request.user.client)
        client = Client.objects.get(user=request.user)

    current_user = request.user
    order_product = OrderProduct.objects.filter(user_id=current_user.id)[:1]
    order_product_count = order_product.count()
    brands = Brands.objects.filter(status='True').order_by('?')
    context = {
        'profile_form': profile_form,
        'user_form': user_form,
        'client': client,
        'order_product': order_product,
        'order_product_count': order_product_count,
        'brands': brands,
    }
    return render(request, 'Client/page-account.html', context)


# - - - - - - - - - - - - - - - LOGOUT - - - - - - - - - - - - - - - #

def logout_form(request):
    logout(request)
    return redirect('home')


# - - - - - - - - - - - - - - - PASSWORD UPDATE - - - - - - - - - - - - - - - #

@login_required(login_url='login_form')
def user_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('creator')
        else:
            messages.error(request, 'Error password')
            return redirect('user_password')
    else:
        form = PasswordChangeForm(request.user)
        creator = Creator.objects.get(user=request.user)
        brands = Brands.objects.filter(status='True').order_by('?')
        context = {
            'form': form,
            'creator': creator,
            'brands': brands,
        }
        return render(request, 'Authenticate/user_password.html', context)


# - - - - - - - - - - - - - - - USER UPDATE - - - - - - - - - - - - - - - #


def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileCreatorUpdateForm(request.POST, request.FILES, instance=request.user.creator)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated')
            return redirect('creator')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileCreatorUpdateForm(instance=request.user.creator)
        creator = Creator.objects.get(user=request.user)
        brands = Brands.objects.filter(status='True').order_by('?')
        context = {
            'user_form': user_form,
            'profile_form': profile_form,
            'creator': creator,
            'brands': brands,
        }
        return render(request, 'Authenticate/user_update.html', context)


# - - - - - - - - - - - - - - - INFORMATION - - - - - - - - - - - - - - - #

def information_add(request):
    if request.method == 'POST':
        form = AddInformationForm(request.POST, request.FILES)
        if form.is_valid():
            information = Informations()
            information.title_uz = form.cleaned_data.get('title_uz')
            information.title_en = form.cleaned_data.get('title_en')
            information.title_ru = form.cleaned_data.get('title_ru')
            information.country = form.cleaned_data.get('country')
            information.city = form.cleaned_data.get('city')
            information.address_en = form.cleaned_data.get('address_en')
            information.address_ru = form.cleaned_data.get('address_ru')
            information.address_uz = form.cleaned_data.get('address_uz')
            information.phone = form.cleaned_data.get('phone')
            information.email = form.cleaned_data.get('email')
            information.telegram = form.cleaned_data.get('telegram')
            information.instagram = form.cleaned_data.get('instagram')
            information.facebook = form.cleaned_data.get('facebook')
            information.twitter = form.cleaned_data.get('twitter')
            information.location = form.cleaned_data.get('location')
            if request.FILES:
                information.logo = request.FILES['icon']
            if request.FILES:
                information.icon = request.FILES['logo']
            information.description_uz = form.cleaned_data.get('description_uz')
            information.description_en = form.cleaned_data.get('description_en')
            information.description_ru = form.cleaned_data.get('description_ru')
            information.status = form.cleaned_data.get('status')
            information.save()
            messages.success(request, 'Your account has been updated')
            return redirect('information_update')
        else:
            messages.error(request, 'Error password')
            return redirect('information_add')
    form = AddInformationForm()
    creator = Creator.objects.get(user=request.user)
    context = {
        'form': form,
        'creator': creator,
    }
    return render(request, 'Information/information_add.html', context)


def information_update(request):
    information = Informations.objects.filter(status='True').order_by('-id')
    creator = Creator.objects.get(user=request.user)
    paginator = Paginator(information, 1)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        information = paginator.page(page)
    except PageNotAnInteger:
        information = paginator.page(1)
    except EmptyPage:
        information = paginator.page(paginator.num_pages)
    context = {
        'information': information,
        'creator': creator,
    }
    return render(request, 'Information/information_update.html', context)


def information_edit(request, id):
    information = Informations.objects.get(pk=id)
    creator = Creator.objects.get(user=request.user)
    if request.method == 'POST':
        form = EditInformationForm(request.POST, request.FILES, instance=information)
        if request.FILES:
            information.image = request.FILES['image']
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been updated')
            return redirect('information_update')
        else:
            messages.error(request, 'Error password')
            return redirect("information_edit")
    else:
        form = EditInformationForm(instance=information)
        context = {
            'form': form,
            'creator': creator,
            'information': information,
        }
        return render(request, 'Information/information_edit.html', context)


def information_delete(request, id):
    information = Informations.objects.get(pk=id)
    information.delete()
    return redirect('information_update')


def information_delete_all(request):
    information = Informations.objects.all()
    information.delete()
    return redirect('information_update')


# - - - - - - - - - - - - - - - CATEGORY - - - - - - - - - - - - - - - #

def category_add(request):
    if request.method == 'POST':
        form = AddCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            category = Category()
            category.title_uz = form.cleaned_data.get('title_uz')
            category.title_en = form.cleaned_data.get('title_en')
            category.title_ru = form.cleaned_data.get('title_ru')
            category.description_uz = form.cleaned_data.get('description_uz')
            category.description_en = form.cleaned_data.get('description_en')
            category.description_ru = form.cleaned_data.get('description_ru')
            if request.FILES:
                category.image = request.FILES['image']
            category.slug = form.cleaned_data.get('slug')
            category.status = form.cleaned_data.get('status')
            category.save()
            return redirect('category_update')
    form = AddCategoryForm()
    creator = Creator.objects.get(user=request.user)
    context = {
        'form': form,
        'creator': creator,
    }
    return render(request, 'Category/category_add.html', context)


def category_update(request):
    category = Category.objects.all()
    creator = Creator.objects.get(user=request.user)
    paginator = Paginator(category, 1)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        category = paginator.page(page)
    except PageNotAnInteger:
        category = paginator.page(1)
    except EmptyPage:
        category = paginator.page(paginator.num_pages)
    context = {
        'category': category,
        'creator': creator,
    }
    return render(request, 'Category/category_update.html', context)


def category_edit(request, id):
    category = Category.objects.get(pk=id)
    creator = Creator.objects.get(user=request.user)
    if request.method == 'POST':
        form = EditCategoryForm(request.POST, request.FILES, instance=category)
        if request.FILES:
            category.image = request.FILES['image']
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been updated')
            return redirect('category_update')
        else:
            messages.error(request, 'Error password')
            return redirect('category_edit')
    else:
        form = EditCategoryForm(instance=category)
        context = {
            'form': form,
            'creator': creator,
            'category': category,
        }
        return render(request, 'Category/category_edit.html', context)


def category_delete(request, id):
    category = Category.objects.get(pk=id)
    category.delete()
    return redirect('category_update')


def category_delete_all(request):
    category = Category.objects.all()
    category.delete()
    return redirect('category_update')


# - - - - - - - - - - - - - - - PRODUCT - - - - - - - - - - - - - - - #

def product_add(request):
    if request.method == 'POST':
        form = AddProductsForm(request.POST, request.FILES)
        if form.is_valid():
            product = Product()
            product.category = form.cleaned_data.get('category')
            product.title_en = form.cleaned_data.get('title_en')
            product.title_ru = form.cleaned_data.get('title_ru')
            product.title_uz = form.cleaned_data.get('title_uz')
            product.old_price = form.cleaned_data.get('old_price')
            product.sell_price = form.cleaned_data.get('sell_price')
            if request.FILES:
                product.image = request.FILES['image']
            product.slug = form.cleaned_data.get('slug')
            product.status = form.cleaned_data.get('status')
            product.description_en = form.cleaned_data.get('description_en')
            product.description_ru = form.cleaned_data.get('description_ru')
            product.description_uz = form.cleaned_data.get('description_uz')
            product.save()
            return redirect('product_update')
    form = AddProductsForm()
    creator = Creator.objects.get(user=request.user)
    context = {
        'form': form,
        'creator': creator,
    }
    return render(request, 'Product/product_add.html', context)


def product_update(request):
    product = Product.objects.all()
    creator = Creator.objects.get(user=request.user)
    paginator = Paginator(product, 1)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        product = paginator.page(page)
    except PageNotAnInteger:
        product = paginator.page(1)
    except EmptyPage:
        product = paginator.page(paginator.num_pages)
    context = {
        'product': product,
        'creator': creator,
    }
    return render(request, 'Product/product_update.html', context)


def product_edit(request, id):
    product = Product.objects.get(pk=id)
    creator = Creator.objects.get(user=request.user)
    if request.method == 'POST':
        form = EditProductsForm(request.POST, request.FILES, instance=product)
        if request.FILES:
            product.image = request.FILES['image']
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been updated')
            return redirect('product_update')
        else:
            messages.error(request, 'Error password')
            return redirect('product_edit')
    else:
        form = EditProductsForm(instance=product)
        context = {
            'form': form,
            'creator': creator,
            'product': product,
        }

        return render(request, 'Product/product_edit.html', context)


def product_delete(request, id):
    product = Product.objects.get(pk=id)
    product.delete()
    return redirect('product_update')


def product_delete_all(request):
    product = Product.objects.all()
    product.delete()
    return redirect('product_update')


# - - - - - - - - - - - - - - - ORDER - - - - - - - - - - - - - - - #

def order_all(request):
    order_all = OrderProduct.objects.all()
    creator = Creator.objects.get(user=request.user)
    paginator = Paginator(order_all, 1)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        order_all = paginator.page(page)
    except PageNotAnInteger:
        order_all = paginator.page(1)
    except EmptyPage:
        order_all = paginator.page(paginator.num_pages)
    context = {
        'order_all': order_all,
        'creator': creator,
    }
    return render(request, 'Orders/orders_page.html', context)


def orders(request, id):
    order_product = OrderProduct.objects.get(pk=id)
    creator = Creator.objects.get(user=request.user)
    if request.method == 'POST':
        form = EditOrderProductForm(request.POST, instance=order_product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been updated')
            return redirect('order_all')
        else:
            messages.error(request, 'Error password')
            return redirect('order_all')
    else:
        form = EditOrderProductForm(instance=order_product)
    context = {
        'form': form,
        'order_product': order_product,
        'creator': creator,
    }
    return render(request, 'Orders/order_detail.html', context)


def order_delete(request, pk):
    order_product = OrderProduct.objects.get(id=pk)
    order = Order.objects.get(id=pk)
    order_product.delete()
    order.delete()
    return redirect('order_all')


def order_delete_all(request):
    order_product = OrderProduct.objects.all()
    order = Order.objects.all()
    order_product.delete()
    order.delete()
    return redirect('order_all')


# - - - - - - - - - - - - - - - DETAIL [ IMAGES ] - - - - - - - - - - - - - - - #

def detail_add(request):
    if request.method == 'POST':
        form = AppandDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            details = Images()
            details.product = form.cleaned_data.get('product')
            if request.FILES:
                details.image = request.FILES['image']
            details.collor = form.cleaned_data.get('collor')
            details.size = form.cleaned_data.get('size')
            details.save()
            return redirect('detail_update')
    form = AppandDetailsForm()
    creator = Creator.objects.get(user=request.user)
    context = {
        'form': form,
        'creator': creator,
    }
    return render(request, 'Details/detail_add.html', context)


def detail_update(request):
    detail = Images.objects.all()
    creator = Creator.objects.get(user=request.user)
    paginator = Paginator(detail, 1)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        detail = paginator.page(page)
    except PageNotAnInteger:
        detail = paginator.page(1)
    except EmptyPage:
        detail = paginator.page(paginator.num_pages)
    context = {
        'detail': detail,
        'creator': creator,
    }
    return render(request, 'Details/detail_update.html', context)


def detail_edit(request, id):
    detail = Images.objects.get(pk=id)
    creator = Creator.objects.get(user=request.user)
    if request.method == 'POST':
        form = EditDetailsForm(request.POST, request.FILES, instance=detail)
        if request.FILES:
            detail.image = request.FILES['image']
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been updated')
            return redirect('detail_update')
        else:
            messages.error(request, 'Error password')
            return redirect('detail_edit')
    else:
        form = EditDetailsForm(instance=detail)
        context = {
            'form': form,
            'creator': creator,
            'detail': detail,
        }

        return render(request, 'Details/detail_edit.html', context)


def detail_delete(request, id):
    detail = Images.objects.get(pk=id)
    detail.delete()
    return redirect('detail_update')


def detail_delete_all(request):
    detail = Images.objects.all()
    detail.delete()
    return redirect('detail_update')


# - - - - - - - - - - - - - - - NEWS - - - - - - - - - - - - - - - #

def news_add(request):
    if request.method == 'POST':
        form = AppandNewsForm(request.POST, request.FILES)
        if form.is_valid():
            news = Blog()
            news.title_uz = form.cleaned_data.get('title_uz')
            news.title_en = form.cleaned_data.get('title_en')
            news.title_ru = form.cleaned_data.get('title_ru')
            if request.FILES:
                news.image = request.FILES['image']
            news.status = form.cleaned_data.get('status')
            news.description_uz = form.cleaned_data.get('description_uz')
            news.description_en = form.cleaned_data.get('description_en')
            news.description_ru = form.cleaned_data.get('description_ru')
            news.save()
            return redirect('news_update')
    form = AppandNewsForm()
    creator = Creator.objects.get(user=request.user)
    context = {
        'form': form,
        'creator': creator,
    }
    return render(request, 'News/news_add.html', context)


def news_update(request):
    news = Blog.objects.all()
    creator = Creator.objects.get(user=request.user)
    paginator = Paginator(news, 1)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    context = {
        'news': news,
        'creator': creator,
    }
    return render(request, 'News/news_update.html', context)


def news_edit(request, id):
    news = Blog.objects.get(pk=id)
    creator = Creator.objects.get(user=request.user)
    if request.method == 'POST':
        form = EditNewsForm(request.POST, request.FILES, instance=news)
        if request.FILES:
            news.image = request.FILES['image']
        if form.is_valid():
            form.save()
            messages.success(request, 'Your news has been updated')
            return redirect('news_update')
        else:
            messages.error(request, 'Error password')
            return redirect('news_edit')
    else:
        form = EditNewsForm(instance=news)
        context = {
            'form': form,
            'creator': creator,
            'blog': news,
        }

        return render(request, 'News/news_edit.html', context)


def news_delete(request, id):
    news = Blog.objects.get(pk=id)
    news.delete()
    return redirect('news_update')


def news_delete_all(request):
    news = Blog.objects.all()
    news.delete()
    return redirect('news_update')


# - - - - - - - - - - - - - - - ABOUT - - - - - - - - - - - - - - - #

def about_add(request):
    if request.method == 'POST':
        form = AppandAboutForm(request.POST, request.FILES)
        if form.is_valid():
            about = Aboutus()
            about.title_uz = form.cleaned_data.get('title_uz')
            about.title_en = form.cleaned_data.get('title_en')
            about.title_ru = form.cleaned_data.get('title_ru')
            if request.FILES:
                about.image = request.FILES['image']
            about.status = form.cleaned_data.get('status')
            about.description_uz = form.cleaned_data.get('description_uz')
            about.description_en = form.cleaned_data.get('description_en')
            about.description_ru = form.cleaned_data.get('description_ru')
            about.save()
            return redirect('about_update')
    form = AppandAboutForm()
    creator = Creator.objects.get(user=request.user)
    context = {
        'form': form,
        'creator': creator,
    }
    return render(request, 'About_us/about_add.html', context)


def about_update(request):
    about = Aboutus.objects.filter(status='True')
    creator = Creator.objects.get(user=request.user)
    paginator = Paginator(about, 1)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        about = paginator.page(page)
    except PageNotAnInteger:
        about = paginator.page(1)
    except EmptyPage:
        about = paginator.page(paginator.num_pages)
    context = {
        'about': about,
        'creator': creator,
    }
    return render(request, 'About_us/about_update.html', context)


def about_edit(request, id):
    about = Aboutus.objects.get(pk=id)
    creator = Creator.objects.get(user=request.user)
    if request.method == 'POST':
        form = EditAboutForm(request.POST, request.FILES, instance=about)
        if request.FILES:
            about.image = request.FILES['image']
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been updated')
            return redirect('about_update')
        else:
            messages.error(request, 'Error password')
            return redirect('about_edit')
    else:
        form = EditAboutForm(instance=about)
        context = {
            'form': form,
            'creator': creator,
            'about': about,
        }

        return render(request, 'About_us/about_edit.html', context)


def about_delete(request, id):
    about = Aboutus.objects.get(pk=id)
    about.delete()
    return redirect('about_update')


def about_delete_all(request):
    about = Aboutus.objects.all()
    about.delete()
    return redirect('about_update')


# - - - - - - - - - - - - - - - FAQ - - - - - - - - - - - - - - - #

def faq_add(request):
    if request.method == 'POST':
        form = AppandFAQSForm(request.POST)
        if form.is_valid():
            faq = Faq()
            faq.ordernumber = form.cleaned_data.get('ordernumber')
            faq.question_en = form.cleaned_data.get('question_en')
            faq.question_ru = form.cleaned_data.get('question_ru')
            faq.question_uz = form.cleaned_data.get('question_uz')
            faq.status = form.cleaned_data.get('status')
            faq.answer_uz = form.cleaned_data.get('answer_uz')
            faq.answer_en = form.cleaned_data.get('answer_en')
            faq.answer_ru = form.cleaned_data.get('answer_ru')
            faq.save()
            return redirect('faq_update')
    form = AppandFAQSForm()
    creator = Creator.objects.get(user=request.user)
    context = {
        'form': form,
        'creator': creator,
    }
    return render(request, 'Faq/faq_add.html', context)


def faq_update(request):
    faq = Faq.objects.filter(status='True').order_by('-id')
    creator = Creator.objects.get(user=request.user)
    paginator = Paginator(faq, 1)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        faq = paginator.page(page)
    except PageNotAnInteger:
        faq = paginator.page(1)
    except EmptyPage:
        faq = paginator.page(paginator.num_pages)
    context = {
        'faq': faq,
        'creator': creator,
    }
    return render(request, 'Faq/faq_update.html', context)


def faq_edit(request, id):
    faq = Faq.objects.get(pk=id)
    creator = Creator.objects.get(user=request.user)
    if request.method == 'POST':
        form = EditFAQSForm(request.POST, request.FILES, instance=faq)
        if request.FILES:
            faq.image = request.FILES['image']
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been updated')
            return redirect('faq_update')
        else:
            messages.error(request, 'Error password')
            return redirect('faq_edit')
    else:
        form = EditFAQSForm(instance=faq)
        context = {
            'form': form,
            'creator': creator,
            'faq': faq,
        }
        return render(request, 'Faq/faq_edit.html', context)


def faq_delete(request, id):
    faq = Faq.objects.get(pk=id)
    faq.delete()
    return redirect('faq_update')


def faq_delete_all(request):
    faq = Faq.objects.all()
    faq.delete()
    return redirect('faq_update')


# - - - - - - - - - - - - - - - NEWSLETTER - - - - - - - - - - - - - - - #

def newsletter_get(request):
    newsletter = NewsLatter.objects.all()
    creator = Creator.objects.get(user=request.user)
    paginator = Paginator(newsletter, 1)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        newsletter = paginator.page(page)
    except PageNotAnInteger:
        newsletter = paginator.page(1)
    except EmptyPage:
        newsletter = paginator.page(paginator.num_pages)
    context = {
        'newsletter': newsletter,
        'creator': creator,
    }
    return render(request, 'Newsletter/newsletter_get.html', context)


def newsletter_delete(request, id):
    newsletter = NewsLatter.objects.get(pk=id)
    newsletter.delete()
    return redirect('newsletter_get')


def newsletter_delete_all(request):
    newsletter = NewsLatter.objects.all()
    newsletter.delete()
    return redirect('newsletter_get')


# - - - - - - - - - - - - - - - CONTACT - - - - - - - - - - - - - - - #

def contact_get(request):
    contact = ContactMessage.objects.all()
    creator = Creator.objects.get(user=request.user)
    paginator = Paginator(contact, 1)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        contact = paginator.page(page)
    except PageNotAnInteger:
        contact = paginator.page(1)
    except EmptyPage:
        contact = paginator.page(paginator.num_pages)
    context = {
        'contact': contact,
        'creator': creator,
    }
    return render(request, 'Contact/contact_get.html', context)


def contact_edit(request, id):
    contact = ContactMessage.objects.get(pk=id)
    creator = Creator.objects.get(user=request.user)
    if request.method == 'POST':
        form = EditContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been updated')
            return redirect('contact_get')
        else:
            messages.error(request, 'Error password')
            return redirect('contact_edit')
    else:
        form = EditContactForm(instance=contact)
        context = {
            'form': form,
            'creator': creator,
            'contact': contact,
        }

        return render(request, 'Contact/contact_edit.html', context)


def contact_delete(request, id):
    contact = ContactMessage.objects.get(pk=id)
    contact.delete()
    return redirect('contact_get')


def contact_delete_all(request):
    contact = ContactMessage.objects.all()
    contact.delete()
    return redirect('contact_get')


# - - - - - - - - - - - - - - - NEWS COMMENT - - - - - - - - - - - - - - - #

def news_comment_get(request):
    comment = Comment_blog.objects.all()
    creator = Creator.objects.get(user=request.user)
    paginator = Paginator(comment, 1)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        comment = paginator.page(page)
    except PageNotAnInteger:
        comment = paginator.page(1)
    except EmptyPage:
        comment = paginator.page(paginator.num_pages)
    context = {
        'comment': comment,
        'creator': creator,
    }
    return render(request, 'News_comment/news_comment_get.html', context)


def news_comment_edit(request, id):
    comment = Comment_blog.objects.get(pk=id)
    creator = Creator.objects.get(user=request.user)
    if request.method == 'POST':
        form = EditNewsCommentForm(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been updated')
            return redirect('news_comment_get')
        else:
            messages.error(request, 'Error password')
            return redirect('news_comment_edit')
    else:
        form = EditNewsCommentForm(instance=comment)
        context = {
            'form': form,
            'creator': creator,
            'comment': comment,
        }

        return render(request, 'News_comment/news_comment_edit.html', context)


def news_comment_delete(request, id):
    news_comment = Comment_blog.objects.get(pk=id)
    news_comment.delete()
    return redirect('news_comment_get')


def news_comment_delete_all(request):
    news_comment = Comment_blog.objects.all()
    news_comment.delete()
    return redirect('news_comment_get')


# - - - - - - - - - - - - - - - PRODUCT COMMENT - - - - - - - - - - - - - - - #

def product_comment_get(request):
    product_comment = Comment.objects.all()
    creator = Creator.objects.get(user=request.user)
    paginator = Paginator(product_comment, 1)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        product_comment = paginator.page(page)
    except PageNotAnInteger:
        product_comment = paginator.page(1)
    except EmptyPage:
        product_comment = paginator.page(paginator.num_pages)
    context = {
        'product_comment': product_comment,
        'creator': creator,
    }
    return render(request, 'Product_comment/product_comment_get.html', context)


def product_comment_edit(request, id):
    product_edit = Comment.objects.get(pk=id)
    creator = Creator.objects.get(user=request.user)
    if request.method == 'POST':
        form = EditProductCommentForm(request.POST, instance=product_edit)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your comment has been updated')
            return redirect('product_comment_get')
        else:
            messages.error(request, 'Error password')
            return redirect('product_comment_edit')
    else:
        form = EditProductCommentForm(instance=product_edit)
        context = {
            'form': form,
            'creator': creator,
            'product_edit': product_edit,
        }

        return render(request, 'Product_comment/product_comment_edit.html', context)


def product_comment_delete(request, id):
    product_comment = Comment.objects.get(pk=id)
    product_comment.delete()
    return redirect('product_comment_get')


def product_comment_delete_all(request):
    product_comment = Comment.objects.all()
    product_comment.delete()
    return redirect('product_comment_get')


# - - - - - - - - - - - - - - - USER PERMISSION - - - - - - - - - - - - - - - #

def user_add_permission(request, id):
    if request.method == 'POST':
        form = UserPermissonForm(request.POST, request.FILES)
        if form.is_valid():
            creator = Creator()
            creator.user = form.cleaned_data.get('user')
            # creator.phone = form.cleaned_data.get('phone')
            # creator.address = form.cleaned_data.get('address')
            # creator.city = form.cleaned_data.get('city')
            if request.FILES:
                creator.image = request.FILES['image']
            # creator.country = form.cleaned_data.get('country')
            client = Client.objects.get(pk=id)
            client.delete()
            creator.save()
            return redirect('creator')
    form = UserPermissonForm()
    client = Client.objects.get(pk=id)
    creator = Creator.objects.get(user=request.user)
    context = {
        'form': form,
        'creator': creator,
        'client': client,
    }
    return render(request, 'Creator_add/add_user_permission.html', context)


def users_get(request):
    users = Client.objects.all()
    creator = Creator.objects.get(user=request.user)
    paginator = Paginator(users, 1)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    context = {
        'users': users,
        'creator': creator,
    }
    return render(request, 'Creator_add/get_users.html', context)


def users_delete(request, id):
    client = Client.objects.get(pk=id)
    client.delete()
    return redirect('users_get')


def users_delete_all(request):
    client = Client.objects.all()
    client.delete()
    return redirect('users_get')


# - - - - - - - - - - - - - - - PRODUCT GALLERY - - - - - - - - - - - - - - - #

def product_gallery(request):
    product = Product.objects.all()
    creator = Creator.objects.get(user=request.user)
    paginator = Paginator(product, 2)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        product = paginator.page(page)
    except PageNotAnInteger:
        product = paginator.page(1)
    except EmptyPage:
        product = paginator.page(paginator.num_pages)
    context = {
        'product': product,
        'creator': creator,
    }
    return render(request, 'Product_gallery/gallery.html', context)


def product_gallery_id(request, id):
    product = Product.objects.get(pk=id)
    images = Images.objects.filter(product_id=id)
    creator = Creator.objects.get(user=request.user)
    context = {
        'product': product,
        'creator': creator,
        'images': images,
    }
    return render(request, 'Product_gallery/gallery_id.html', context)


# - - - - - - - - - - - - - - - SLIDER - - - - - - - - - - - - - - - #

def slider_add(request):
    if request.method == 'POST':
        form = AppandSliderForm(request.POST, request.FILES)
        if form.is_valid():
            slider = Slider()
            slider.title_en = form.cleaned_data.get('title_en')
            slider.title_ru = form.cleaned_data.get('title_ru')
            slider.title_uz = form.cleaned_data.get('title_uz')
            if request.FILES:
                slider.image = request.FILES['image']
            slider.description_uz = form.cleaned_data.get('description_uz')
            slider.description_en = form.cleaned_data.get('description_en')
            slider.description_ru = form.cleaned_data.get('description_ru')
            slider.save()
            return redirect('slider_update')
    form = AppandSliderForm()
    creator = Creator.objects.get(user=request.user)
    context = {
        'form': form,
        'creator': creator,
    }
    return render(request, 'Slider/slider_add.html', context)


def slider_update(request):
    slider = Slider.objects.filter(status='True').order_by('-id')
    creator = Creator.objects.get(user=request.user)
    paginator = Paginator(slider, 1)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        slider = paginator.page(page)
    except PageNotAnInteger:
        slider = paginator.page(1)
    except EmptyPage:
        slider = paginator.page(paginator.num_pages)
    context = {
        'slider': slider,
        'creator': creator,
    }
    return render(request, 'Slider/slider_update.html', context)


def slider_edit(request, id):
    slider = Slider.objects.get(pk=id)
    creator = Creator.objects.get(user=request.user)
    if request.method == 'POST':
        form = EditSliderForm(request.POST, instance=slider)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been updated')
            return redirect('slider_update')
        else:
            messages.error(request, 'Error password')
            return redirect('slider_edit')
    else:
        form = EditSliderForm(instance=slider)
        context = {
            'form': form,
            'creator': creator,
            'slider': slider,
        }

        return render(request, 'Slider/slider_edit.html', context)


def slider_delete(request, id):
    slider = Slider.objects.get(pk=id)
    slider.delete()
    return redirect('slider_update')


def slider_delete_all(request):
    slider = Slider.objects.all()
    slider.delete()
    return redirect('slider_update')


# - - - - - - - - - - - - - - - reklama - - - - - - - - - - - - - - - #

def add_adversiting(request):
    if request.method == 'POST':
        form = AppandAversitingForm(request.POST, request.FILES)
        if form.is_valid():
            adversiting = Adversiting()
            adversiting.title_en = form.cleaned_data.get('title_en')
            adversiting.title_ru = form.cleaned_data.get('title_ru')
            adversiting.title_uz = form.cleaned_data.get('title_uz')
            if request.FILES:
                adversiting.image = request.FILES['image']
            adversiting.status = form.cleaned_data.get('status')
            adversiting.save()
            return redirect('adversiting_update')
    form = AppandAversitingForm()
    creator = Creator.objects.get(user=request.user)
    context = {
        'form': form,
        'creator': creator,
    }
    return render(request, 'Adversiting/addadversiting.html', context)


def adversiting_update(request):
    adversiting = Adversiting.objects.filter(status='True').order_by('-id')
    creator = Creator.objects.get(user=request.user)
    paginator = Paginator(adversiting, 1)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        adversiting = paginator.page(page)
    except PageNotAnInteger:
        adversiting = paginator.page(1)
    except EmptyPage:
        adversiting = paginator.page(paginator.num_pages)
    context = {
        'adversiting': adversiting,
        'creator': creator,
    }
    return render(request, 'Adversiting/adversiting_update.html', context)


def adversiting_edit(request, id):
    adversiting = Adversiting.objects.get(pk=id)
    creator = Creator.objects.get(user=request.user)
    if request.method == 'POST':
        form = EditAdversitingForm(request.POST, request.FILES, instance=adversiting)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been updated')
            return redirect('adversiting_update')
        else:
            messages.error(request, 'Error password')
            return redirect('adversiting_edit')
    else:
        form = EditAdversitingForm(instance=adversiting)
        context = {
            'form': form,
            'creator': creator,
            'adversiting': adversiting,
        }

        return render(request, 'Adversiting/adversiting_edit.html', context)


def adversiting_delate(request, id):
    adversiting = Adversiting.objects.get(pk=id)
    adversiting.delete()
    return redirect('adversiting_update')


def adversiting_delate_all(request):
    adversiting = Adversiting.objects.all()
    adversiting.delete()
    return redirect('adversiting_update')


# - - - - - - - - - - - - - - - SEARCH - - - - - - - - - - - - - - - #

def searched(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        product = Product.objects.filter(title__contains=searched)
        category = Category.objects.filter(status='True').order_by('-id')
        context = {
            'category': category,
            'searched': searched,
            'product': product,
        }
        return render(request, 'Searched/searched.html', context)


# - - - - - - - - - - - - - - - LANGUAGE - - - - - - - - - - - - - - - #

def selectlanguage_admin(request):
    if request.method == 'POST':
        cur_language = translation.get_language()
        lasturl = request.META.get('HTTP_REFERER')
        lang = request.POST['language']
        translation.activate(lang)
        request.session['translation.LANGUAGE_SESSION_KEY'] = lang
        return redirect("creator")


def selectlanguage_client(request):
    if request.method == 'POST':
        cur_language = translation.get_language()
        lasturl = request.META.get('HTTP_REFERER')
        lang = request.POST['language']
        translation.activate(lang)
        request.session['translation.LANGUAGE_SESSION_KEY'] = lang
        return redirect("client")


# - - - - - - - - - - - - - - - BRAND - - - - - - - - - - - - - - - #

def add_brand(request):
    if request.method == 'POST':
        form = AppandBrandForm(request.POST, request.FILES)
        if form.is_valid():
            brand = Brands()
            brand.title_en = form.cleaned_data.get('title_en')
            brand.title_ru = form.cleaned_data.get('title_ru')
            brand.title_uz = form.cleaned_data.get('title_uz')
            if request.FILES:
                brand.image = request.FILES['image']
            brand.status = form.cleaned_data.get('status')
            brand.save()
            return redirect('creator')
    form = AppandBrandForm()
    creator = Creator.objects.get(user=request.user)
    context = {
        'form': form,
        'creator': creator,
    }
    return render(request, 'Brands/add_brands.html', context)


def brand_update(request):
    brand = Brands.objects.filter(status='True').order_by('-id')
    creator = Creator.objects.get(user=request.user)
    paginator = Paginator(brand, 1)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        brand = paginator.page(page)
    except PageNotAnInteger:
        brand = paginator.page(1)
    except EmptyPage:
        brand = paginator.page(paginator.num_pages)
    context = {
        'brand': brand,
        'creator': creator,
    }
    return render(request, 'Brands/brand_update.html', context)


def brand_edit(request, id):
    brand = Brands.objects.get(pk=id)
    creator = Creator.objects.get(user=request.user)
    if request.method == 'POST':
        form = EditBrandForm(request.POST, instance=brand)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been updated')
            return redirect('brand_update')
        else:
            messages.error(request, 'Error password')
            return redirect('brand_edit')
    else:
        form = EditBrandForm(instance=brand)
        context = {
            'form': form,
            'creator': creator,
            'brand': brand,
        }

        return render(request, 'Brands/brand_edit.html', context)


def brand_delate(request, id):
    brand = Adversiting.objects.get(pk=id)
    brand.delete()
    return redirect('brand_update')


def brand_delate_all(request):
    brand = Adversiting.objects.all()
    brand.delete()
    return redirect('brand_update')


# - - - - - - - - - - - - - - - Search - - - - - - - - - - - - - - - #

def search_dashbourd(request):
    if request.method == 'POST':
        searched = request.POST['search']
        product = Product.objects.filter(title__contains=searched)
        product_count = product.count()
        category = Category.objects.filter(status='TRUE')
        creator = Creator.objects.get(user=request.user)
        info = Informations.objects.all().order_by('-id')[:1]
        brands = Brands.objects.filter(status='True').order_by('?')
        context = {
            'searched': searched,
            'product': product,
            'product_count': product_count,
            'category': category,
            'creator': creator,
            'info': info,
            'brands': brands,
        }
        return render(request, 'Searched/dashbourd_search.html', context)
