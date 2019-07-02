from django.test import TestCase
from answer.models import Product


class ProductTestCase(TestCase):

    def setUp(self):

        Product.objects.create(name="Bâtonnets sablés chocolat au lait", id=1295, nutriscore='e',
                               link='https://fr.openfoodfacts.org/produit/3350033111868/batonnets-sables-chocolat-au-lait-monoprix-gourmet',
                               category='Snacks', picture='https://static.openfoodfacts.org/images/products/335/003/311/1868/front_fr.27.400.jpg')

        Product.objects.create(name='Gâteau au chocolat noir', nutriscore='d', category='Snacks')
        Product.objects.create(name='Chocolat Lait', nutriscore='e', category='Snacks')
        Product.objects.create(name='Chocolat Lait', nutriscore='b', category='Desserts')
        Product.objects.create(name='Bâtonnets de chocolat', nutriscore='e', category='Snacks')
        Product.objects.create(name='Croustifondante Chocolat', nutriscore='e', category='Snacks')
        Product.objects.create(name='Ferme & Fondant Chocolat', nutriscore='b', category='Snacks')
        Product.objects.create(name='Delichoc', nutriscore='e', category='Snacks')
        Product.objects.create(name='Délichoc sablé', nutriscore='e', category='Snacks')
        Product.objects.create(name='Savane Le Classique Chocolat', nutriscore='d', category='Snacks')
        Product.objects.create(name='Biscuits nappés chocolat noir', nutriscore='d', category='Snacks')
        Product.objects.create(name='BN goût chocolat', nutriscore='e', category='Snacks')
        Product.objects.create(name='Biscuit Avoine et Chocolat', nutriscore='e', category='Snacks')
        Product.objects.create(name='Fitness Chocolat Noir', nutriscore='c', category='Snacks')
        Product.objects.create(name='Kinder chocolat mini eggs', nutriscore='e', category='Snacks')
        Product.objects.create(name='Chocolat Happy', nutriscore='e', category='Snacks')
        Product.objects.create(name='Kinder Chocolat', nutriscore='e', category='Snacks')
        Product.objects.create(name='Bitter Schokolade', nutriscore='e', category='Snacks')
        Product.objects.create(name='Petit-beurre Chocolat Noir', nutriscore='e', category='Snacks')
        Product.objects.create(name='Biscuit choco fondant noir', nutriscore='d', category='Snacks')

    def test_find_similar_name(self):
        query = "lait chocolat"
        result = ['Gâteau au chocolat noir', 'Chocolat Lait', 'Chocolat Lait', 'Bâtonnets de chocolat', 'Croustifondante Chocolat',
                  'Ferme & Fondant Chocolat', 'Delichoc', 'Délichoc sablé', 'Savane Le Classique Chocolat',
                  'Biscuits nappés chocolat noir', 'BN goût chocolat', 'Biscuit Avoine et Chocolat',
                  'Fitness Chocolat Noir', 'Kinder chocolat mini eggs', 'Chocolat Happy', 'Kinder Chocolat',
                  'Bitter Schokolade', 'Petit-beurre Chocolat Noir', 'Biscuit choco fondant noir']
        function_output = Product.find_similar_name(Product(), query)
        self.assertEqual(function_output, result)

    def test_product_chosen(self):
        query = "bâtonnets Sablés Chocolat Au Lait"

        name = "Bâtonnets sablés chocolat au lait"
        picture = 'https://static.openfoodfacts.org/images/products/335/003/311/1868/front_fr.27.400.jpg'
        nutriscore = 'e'
        category = 'Snacks'
        link = 'https://fr.openfoodfacts.org/produit/3350033111868/batonnets-sables-chocolat-au-lait-monoprix-gourmet'
        id = 1295
        result = name, picture, nutriscore, category, link, id

        function_output = Product.product_chosen(Product(), query)
        self.assertEqual(function_output, result)

    def test_product_chosen_sim(self):
        query = 1295

        name = "Bâtonnets sablés chocolat au lait"
        picture = 'https://static.openfoodfacts.org/images/products/335/003/311/1868/front_fr.27.400.jpg'
        nutriscore = 'e'
        category = 'Snacks'
        link = 'https://fr.openfoodfacts.org/produit/3350033111868/batonnets-sables-chocolat-au-lait-monoprix-gourmet'
        id = 1295
        result = name, picture, nutriscore, category, link, id

        function_output = Product.product_chosen_sim(Product(), query)
        self.assertEqual(function_output, result)

    def test_get_same_names(self):
        product_name = "Bâtonnets sablés chocolat au lait"
        product_category = 'Snacks'

        result = ["Bâtonnets sablés chocolat au lait", 'Gâteau au chocolat noir', 'Bâtonnets de chocolat',
                  'Biscuits nappés chocolat noir', 'Fitness Chocolat Noir']

        function_output = Product.get_same_names(Product(), product_name, product_category)
        self.assertEqual(function_output, result)

    def test_get_better_nutriscore(self):
        product_nutriscore = "e"

        result = ['a', 'b', 'c', 'd', 'e']

        function_output = Product.get_better_nutriscore(Product(), product_nutriscore)
        self.assertEqual(function_output, result)

    def test_extract_products_for_replace(self):
        better_nutriscore_list = ['a', 'b', 'c', 'd', 'e']
        product_category = 'Snacks'
        product_link = 'https://fr.openfoodfacts.org/produit/3350033111868/batonnets-sables-chocolat-au-lait-monoprix-gourmet'
        best_ratio_list = ['Bâtonnets sablés chocolat au lait', 'Gâteau au chocolat noir',
                           'Bâtonnets de chocolat']

        better_products = Product.objects.filter(category=product_category).filter(name__in=best_ratio_list). \
            filter(nutriscore__in=better_nutriscore_list).exclude(link=product_link).order_by('name')

        function_output = Product.extract_products_for_replace(Product(), better_nutriscore_list, product_category, best_ratio_list,
                                                               product_link)
        map(function_output, better_products)



