from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from products.views import (goodby_view, hello_view, main_view, now_date_view,
                            products_view)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_view),
    path('now_date/', now_date_view),
    path('goodby/', goodby_view),
    path('', main_view, name='main_page'),
    path('products/', products_view, name='products'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
