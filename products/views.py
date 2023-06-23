from datetime import date

from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from products.forms import CategoryCreateForm, ProductCreateForm
from products.models import Category, Product


def hello_view(request: HttpRequest) -> HttpResponse:
    if request.method != 'GET':
        return HttpResponse('Invalid HTTP method', status=404)
    return HttpResponse('Hello! Its my project')


def now_date_view(request: HttpRequest) -> HttpResponse:
    if request.method != 'GET':
        return HttpResponse('Invalid HTTP method', status=404)
    return HttpResponse(date.today())


def goodby_view(request: HttpRequest) -> HttpResponse:
    if request.method != 'GET':
        return HttpResponse('Invalid HTTP method', status=404)
    return HttpResponse('Goodby user!')


def main_view(request: HttpRequest) -> HttpResponse:
    if request.method != 'GET':
        return HttpResponse('Invalid HTTP method', status=404)

    return render(request, 'layouts/base.html')


def products_view(request: HttpRequest) -> HttpResponse:
    if request.method != 'GET':
        return HttpResponse('Invalid HTTP method', status=404)

    products = Product.objects.all()
    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context=context)


def categories_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = CategoryCreateForm(data=request.POST, files=request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('categories'))
    else:
        form = CategoryCreateForm

    categories = Category.objects.all()
    context = {
        'categories': categories,
        'form': form,
    }

    return render(request, 'products/categories.html', context=context)


def product_detail_view(request: HttpRequest, id: int) -> HttpResponse:
    if request.method != 'GET':
        return HttpResponse('Invalid HTTP method', status=404)

    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return HttpResponse('Page not found', status=404)

    context = {
        'product': product,
    }

    return render(request, 'products/detail.html', context=context)


def create_product_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = ProductCreateForm(data=request.POST, files=request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('products'))
    else:
        form = ProductCreateForm

    context = {
        'form': form,
    }

    return render(request, 'products/create.html', context)
