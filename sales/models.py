from django.db import models
from django.db.models import Sum, Avg
from django.db.models import F, FloatField

class ArticleCategory(models.Model):
    """
    Category of an article
    """

    class Meta:
        verbose_name = "Article Category"
        verbose_name_plural = "Article Categories"

    objects = models.Manager()

    display_name = models.CharField("Display name", unique=True, max_length=255)

    def __str__(self):
        return f"{self.display_name}"


class Article(models.Model):
    """
    An article is an item that can be sold.
    """

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    objects = models.Manager()

    code = models.CharField("Code", max_length=6, unique=True)
    category = models.ForeignKey(
        ArticleCategory,
        verbose_name="Category",
        related_name="articles",
        on_delete=models.PROTECT,
    )
    name = models.CharField("Name", max_length=255)
    manufacturing_cost = models.DecimalField(
        "Manufacturing Cost", max_digits=11, decimal_places=2
    )

    def __str__(self):
        return f"{self.code} - {self.name}"
    
    @property
    def total_selling_price(self):
        ''' 
            Total price sold for this article
             unit_selling_price*quantity in sale Model
        '''
        return Sale.objects.filter(article=self).aggregate(total_selling_price = Sum(F("unit_selling_price")*F("quantity"),output_field=FloatField() ) )["total_selling_price"]


    @property
    def percentage_marge(self):
        '''
            Percentage of profit margin of this article
            unit_selling_price - manufacturing_cost/manufacturing_cost
        '''
        if Sale.objects.filter(article=self).count()>0:
            return round( (Sale.objects.filter(article=self).aggregate(unit_selling_price_avg=Avg(F('unit_selling_price') - F('article__manufacturing_cost') ) ) ['unit_selling_price_avg'] / self.manufacturing_cost)*100 , 2 )
        else:
            return 0

    @property
    def last_article_sold(self):
        '''
            Last article sold
        '''
        return Sale.objects.filter(article=self).values("date").order_by('-date').first()["date"]

class Sale(models.Model):
    """
    A sale of an article.
    """

    class Meta:
        verbose_name = "Sale"
        verbose_name_plural = "Sales"

    objects = models.Manager()

    date = models.DateField("Date")
    author = models.ForeignKey(
        "users.User",
        verbose_name="Author",
        related_name="sales",
        on_delete=models.PROTECT,
    )
    article = models.ForeignKey(
        Article, verbose_name="Article", related_name="sales", on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField("Quantity")
    unit_selling_price = models.DecimalField(
        "Unit selling price", max_digits=11, decimal_places=2
    )

    def __str__(self):
        return f"{self.date} - {self.quantity} {self.article.name}"

    @property
    def total_selling_price(self):
        return self.quantity * self.unit_selling_price
