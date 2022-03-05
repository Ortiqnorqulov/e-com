from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from user.models import Client, Brands
from home.forms import ContactForm, NewsLatterForm
from home.models import ContactMessage, Aboutus, Faq, NewsLatter, Informations, Slider, Wishlist, Adversiting
from order.models import ShopCart
from product.models import Product, Category, Images, Comment
from blog.models import Blog
from django.http import HttpResponseRedirect
from django.utils import translation


################################################################################################################
################################################################################################################
################################################################################################################


def home(request):
    category = Category.objects.all()
    product_slider = Product.objects.filter(status='True').order_by('?')
    product_latest = Product.objects.filter(status='True').order_by('-id')
    product_picked = Product.objects.filter(status='True').order_by('?')[:8]
    blog = Blog.objects.all().order_by('-id')[:3]
    info = Informations.objects.filter(status='True').order_by('-id')[:1]
    slider = Slider.objects.all().order_by('-id')
    brands = Brands.objects.filter(status='True').order_by('-id')
    adversiting = Adversiting.objects.filter(status='True').order_by('?')[:3]
    brands = Brands.objects.filter(status='True').order_by('?')
    context = {
        'category': category,
        'product_slider': product_slider,
        'product_latest': product_latest,
        'product_picked': product_picked,
        'blog': blog,
        'info': info,
        'slider': slider,
        'brands': brands,
        'adversiting': adversiting,
    }
    return render(request, 'index.html', context)


################################################################################################################
################################################################################################################
################################################################################################################


def header(request):
    category = Category.objects.filter(status='True').order_by('id')
    info = Informations.objects.filter(status='True').order_by('-id')[:1]
    slider = Slider.objects.all().order_by('-id')
    brands = Brands.objects.filter(status='True').order_by('?')
    context = {
        'category': category,
        'info': info,
        'slider': slider,
        'brands': brands,
    }
    return render(request, 'header.html', context)


def footer(request):
    category = Category.objects.all()
    info = Informations.objects.filter(status='True').order_by('-id')[:1]
    brands = Brands.objects.filter(status='True').order_by('?')
    context = {
        'category': category,
        'info': info,
        'brands': brands,
    }
    return render(request, 'footer.html', context)


################################################################################################################
################################################################################################################
################################################################################################################


@login_required(login_url='login_form')
def wishlist(request):
    category = Category.objects.all()
    current_user = request.user
    user = Client.objects.get(user=request.user)
    info = Informations.objects.all().order_by('-id')[:1]
    brands = Brands.objects.filter(status='True').order_by('?')
    wishlist = Wishlist.objects.filter(user=user)
    wishlist_all_count = wishlist.count()
    total_qty = 0
    for rs in wishlist:
        total_qty += rs.quantity
    context = {
        'wishlist_all_count': wishlist_all_count,
        'user': user,
        'wishlist': wishlist,
        'category': category,
        'total_qty': total_qty,
        'current_user': current_user,
        'info': info,
        'brands': brands,
    }
    return render(request, 'wishlist.html', context)


@login_required(login_url='login_form')
def deletefromcart(request, id):
    Wishlist.objects.filter(id=id).delete()
    messages.success(request, "Your item deleted from Wishlist!")
    return redirect('wishlist')


################################################################################################################
################################################################################################################
################################################################################################################


def product_detail(request, id, slug):
    category = Category.objects.all()
    product_picked = Product.objects.all().order_by('?')[:8]
    product_latest = Product.objects.all().order_by('-id')[:4]
    product = Product.objects.get(pk=id)
    images = Images.objects.filter(product_id=id)
    info = Informations.objects.all().order_by('-id')[:1]
    comments = Comment.objects.filter(product_id=id, status='True')
    brands = Brands.objects.filter(status='True').order_by('?')
    adversiting = Adversiting.objects.filter(status='True').order_by('?')[:2]
    context = {
        'comments': comments,
        'category': category,
        'product': product,
        'images': images,
        'product_latest': product_latest,
        'product_picked': product_picked,
        'info': info,
        'brands': brands,
        'adversiting': adversiting,
    }
    return render(request, 'product_detail.html', context)


################################################################################################################
################################################################################################################
################################################################################################################


def category_product(request, id, slug):
    category = Category.objects.all()
    categoryies = Category.objects.get(pk=id)
    info = Informations.objects.all().order_by('-id')[:1]
    brands = Brands.objects.filter(status='True').order_by('?')
    product_latest = Product.objects.filter(status='True').order_by('?')[:3]
    products = Product.objects.filter(category_id=id)
    adversiting = Adversiting.objects.filter(status='True').order_by('?')[:2]
    paginator = Paginator(products, 2)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    context = {
        'category': category,
        'products': products,
        'product_latest': product_latest,
        'info': info,
        'categoryies': categoryies,
        'brands': brands,
        'adversiting': adversiting,
    }
    return render(request, 'shop0.html', context)


################################################################################################################
################################################################################################################
################################################################################################################


def contactus(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.surname = form.cleaned_data['surname']
            data.subject = form.cleaned_data['subject']
            data.email = form.cleaned_data['email']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Your message has been sent! Thank you")
            return redirect('home')
    form = ContactForm
    category = Category.objects.all()
    info = Informations.objects.all()[:1]
    brands = Brands.objects.filter(status='True').order_by('-id')
    context = {
        'form': form,
        'category': category,
        'info': info,
        'brands': brands,
    }

    return render(request, 'contact.html', context)


################################################################################################################
################################################################################################################
################################################################################################################


def aboutus(request):
    category = Category.objects.all()
    blog = Blog.objects.all().order_by('?')[:12]
    info = Informations.objects.all().order_by('-id')[:1]
    about = Aboutus.objects.all()
    brands = Brands.objects.filter(status='True').order_by('?')
    context = {
        'blog': blog,
        'about': about,
        'category': category,
        'info': info,
        'brands': brands,

    }
    return render(request, 'about_us.html', context)


################################################################################################################
################################################################################################################
################################################################################################################


def faq(request):
    faq = Faq.objects.all()
    category = Category.objects.all()
    info = Informations.objects.all().order_by('-id')[:1]
    brands = Brands.objects.filter(status='True').order_by('?')
    content = {
        'faq': faq,
        'category': category,
        'info': info,
        'brands': brands,
    }
    return render(request, 'faq1.html', content)


################################################################################################################
################################################################################################################
################################################################################################################


def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        product = Product.objects.filter(title__contains=searched)
        category = Category.objects.filter(status='TRUE')
        info = Informations.objects.all().order_by('-id')[:1]
        brands = Brands.objects.filter(status='True').order_by('?')
        context = {
            'searched': searched,
            'product': product,
            'category': category,
            'info': info,
            'brands': brands,
        }
        return render(request, 'search.html', context)


################################################################################################################
################################################################################################################
################################################################################################################


def newsLatter(request):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = NewsLatterForm(request.POST)
        if form.is_valid():
            data = NewsLatter()
            data.email = form.cleaned_data['email']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Your email has been received!")
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)


def selectlanguage(request):
    if request.method == 'POST':
        cur_language = translation.get_language()
        lasturl = request.META.get('HTTP_REFERER')
        lang = request.POST['language']
        translation.activate(lang)
        request.session['translation.LANGUAGE_SESSION_KEY'] = lang
        return redirect("home")
