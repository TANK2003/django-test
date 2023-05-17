#### ALL ABOUT PYTHON 

#### ALL ABOUT DJANGO 
from django.urls import reverse_lazy, reverse
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

#### ALL ABOUT THIS PROJECT 
from users.models import User
from sales.models import ArticleCategory, Article, Sale


# Create your tests here.
class TestSale(APITestCase):

    url = "/api/v1/sale/"

    @property
    def bearer_token(self):
        refresh = RefreshToken.for_user(self.user)
        return {"HTTP_AUTHORIZATION":f'Bearer {refresh.access_token}'}

    def setUp(self):

        # Create a non admin user
        self.user = User.objects.create_user(
            email='usertest@test.com',
            password='testpass'
        )

        # Create  Sale 
        self.article:Article = Article.objects.create(
            code='ABC123',
            category=ArticleCategory.objects.create(display_name='Category'),
            name='Article fro test',
            manufacturing_cost=100.00
        )

        self.sale:Sale = Sale.objects.create(
            date='2023-05-17',
            author=self.user,
            article=self.article,
            quantity=32,
            unit_selling_price=176.48
        )

      

    def test_create_sale(self):
        """
        Test for creation on a sale.
        """
        sale_data = {
            'date': '2023-05-17',
            'article': self.article.id,
            'quantity': 24,
            'unit_selling_price': 146.00
        }

        response = self.client.post(self.url, data=sale_data, **self.bearer_token)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Sale.objects.count(), 2)
        self.assertEqual(Sale.objects.first().author, self.user)


    def test_update_sale_by_his_author(self):
        """
        Test for author to be able to update his sale
        """

        response = self.client.patch(
            self.url+str(self.sale.pk)+'/',
            {
                'quantity': 43
            }
            , **self.bearer_token
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['quantity'], 43)

    
    def test_list_unauthenticated(self):
        """
        Test list of sale with unauthenticated user
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_authenticated(self):
        """
        Test list of sale with authenticated user
        """
        response = self.client.get(self.url, **self.bearer_token)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


