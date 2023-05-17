#### ALL ABOUT PYTHON 

#### ALL ABOUT DJANGO 
from rest_framework import serializers

#### ALL ABOUT THIS PROJECT 
from sales.models import Sale, Article, ArticleCategory


class ArticleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleCategory
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    category = ArticleCategorySerializer(read_only=True)
    class Meta:
        model = Article
        fields = '__all__'

class ArticleDetailsSerializer(serializers.ModelSerializer):
    category = ArticleCategorySerializer(read_only=True)
    total_selling_price = serializers.FloatField( read_only=True)
    percentage_marge = serializers.DecimalField(max_digits=5, decimal_places=2, read_only=True)
    last_article_sold = serializers.DateField(read_only=True)
    
    class Meta:
        model = Article
        fields = '__all__'

class SaleSerializer(serializers.ModelSerializer):
    article_info = ArticleSerializer(read_only=True, source='article')
    total_selling_price = serializers.FloatField(read_only=True)
    author = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )
        
    class Meta:
        model = Sale
        fields = '__all__'