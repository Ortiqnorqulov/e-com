from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from blog.forms import Comment_detail_Form
from blog.models import Blog, Comment_blog
from django.core.paginator import (Paginator, PageNotAnInteger, EmptyPage)
from home.models import Informations, Adversiting
from product.models import Category, Product
from user.models import Brands, Client


################################################################################################################
################################################################################################################
################################################################################################################



def blog(request):
    info = Informations.objects.all().order_by('-id')[:1]
    blog = Blog.objects.all()
    category = Category.objects.all()
    brands = Brands.objects.filter(status='True').order_by('?')
    paginator = Paginator(blog, 2)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        blog = paginator.page(page)
    except PageNotAnInteger:
        blog = paginator.page(1)
    except EmptyPage:
        blog = paginator.page(paginator.num_pages)
    context = {
        'blog': blog,
        'comment_blog': comment_blog,
        'info': info,
        'brands': brands,
        'category': category,
    }
    return render(request, 'blog.html', context)


################################################################################################################
################################################################################################################
################################################################################################################


def blog_detail(request, id):
    category = Category.objects.all()
    info = Informations.objects.all().order_by('-id')[:1]
    # user = Client.objects.get(user=request.user)
    products = Product.objects.all()
    blog_two = Blog.objects.all().order_by('-id')[:4]
    blog_detail = Blog.objects.get(pk=id)
    comment_blog = Comment_blog.objects.filter(blog_id=id, status='True').order_by('?')[:4]
    brands = Brands.objects.filter(status='True').order_by('?')
    adversiting = Adversiting.objects.filter(status='True').order_by('?')[:2]
    context = {
        'category': category,
        'products': products,
        'blog_detail': blog_detail,
        'comment_blog': comment_blog,
        'blog_two': blog_two,
        'info': info,
        'brands': brands,
        'adversiting': adversiting,
        # 'user': user,
    }
    return render(request, 'blog_details.html', context)


################################################################################################################
################################################################################################################
################################################################################################################


def comment_blog(request, id):
    current_user = request.user
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = Comment_detail_Form(request.POST)
        if form.is_valid():
            data = Comment_blog()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.comment = form.cleaned_data['comment']
            data.ip = request.META.get('REMOTE_ADDR')
            data.blog_id = id
            # data.client_id = id
            data.save()
            messages.success(request, "Your comment has been accepted!")
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)
