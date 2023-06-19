from datetime import date

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

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
    if request.method != 'GET':
        return HttpResponse('Invalid HTTP method', status=404)

    categories = Category.objects.all()
    context = {
        'categories': categories,
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
