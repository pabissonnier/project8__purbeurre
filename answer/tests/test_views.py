from django.test import TestCase, Client
from django.urls import reverse
from answer.models import Product
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

    def test_index_page(self):

        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'answer/index.html')

    def test_search_page(self):
        response = self.client.get(reverse('search-products'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'answer/search.html')

    def test_app_page(self):
        response = self.client.get(reverse('application'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'answer/layout.html')
        self.assertTemplateUsed(response, 'answer/list.html')

    def test_app_sim_page(self): # doesn't work
        """Product.objects.create(name="Bâtonnets sablés chocolat au lait", id=1295, nutriscore='e',
                               link='https://fr.openfoodfacts.org/produit/3350033111868/batonnets-sables-chocolat-au-lait-monoprix-gourmet',
                               category='Snacks',
                               picture='https://static.openfoodfacts.org/images/products/335/003/311/1868/front_fr.27.400.jpg')"""

        response = self.client.get(reverse('application_sim'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'answer/results.html')
