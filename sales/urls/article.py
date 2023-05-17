#### ALL ABOUT PYTHON 

#### ALL ABOUT DJANGO 
from django.urls import include, path

#### ALL ABOUT THIS PROJECT 
from sales.views import ListDetailsArticles
urlpatterns = [
    path("", ListDetailsArticles.as_view(), name="List-details-article"),
]