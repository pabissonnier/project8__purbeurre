from django.test import TestCase, Client
from django.urls import reverse
from answer.models import Product


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.product = Product.objects.create(name="Bâtonnets sablés chocolat au lait", id=1295, nutriscore='e',
                               link='https://fr.openfoodfacts.org/produit/3350033111868/batonnets-sables-chocolat-au-lait-monoprix-gourmet',
                               category='Snacks',
                               picture='https://static.openfoodfacts.org/images/products/335/003/311/1868/front_fr.27.400.jpg')

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

    def test_detail_page_returns_200(self):
        product_id = Product.objects.get(name='Bâtonnets sablés chocolat au lait').id
        response = self.client.get(reverse('detail', args=(product_id,)))
        self.assertEqual(response.status_code, 200)

    def test_detail_page_returns_400(self):
        product_id = Product.objects.get(name='Bâtonnets sablés chocolat au lait').id + 1
        response = self.client.get(reverse('detail', args=(product_id,)))
        self.assertEqual(response.status_code, 404)
