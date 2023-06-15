from django.contrib import admin
from django.urls import path

from products.views import goodby_view, hello_view, now_date_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_view),
    path('now_date/', now_date_view),
    path('goodby/', goodby_view),
]
