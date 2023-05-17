#### ALL ABOUT PYTHON 

#### ALL ABOUT DJANGO 
from django.urls import include, path

#### ALL ABOUT THIS PROJECT 
from sales.views import ListAndCreateSales, UpdateSale

urlpatterns = [
    path("", ListAndCreateSales.as_view(), name="List-create-sale"),
    path("<int:pk>/", UpdateSale.as_view(), name="update-sale"),
]