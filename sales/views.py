#### ALL ABOUT PYTHON 

#### ALL ABOUT DJANGO 
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum
from django.db.models import F, FloatField
#### ALL ABOUT THIS PROJECT 
from sales.models import Sale, Article
from sales.serializers import SaleSerializer, ArticleDetailsSerializer
from main.core.paginations import DefaultResultsSetPagination
from main.core.permissions import CanUpdateSale


# Create your views here.

class ListAndCreateSales(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    pagination_class = DefaultResultsSetPagination
    
class UpdateSale(UpdateAPIView):
    permission_classes = [IsAuthenticated, CanUpdateSale]
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

class ListDetailsArticles(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Article.objects.all().annotate(total = Sum(F("sales__unit_selling_price")*F("sales__quantity"),output_field=FloatField() ) ).order_by('-total')
    serializer_class = ArticleDetailsSerializer