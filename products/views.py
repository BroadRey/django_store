from datetime import date

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def hello_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Hello! Its my project')


def now_date_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse(date.today())


def goodby_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Goodby user!')
