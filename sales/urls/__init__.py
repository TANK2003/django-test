from django.urls import path, include
from django.conf import settings


urlpatterns = [
    path("article/", include("sales.urls.article")),
    path("sale/", include("sales.urls.sale")),
]