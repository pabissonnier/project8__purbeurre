from django.test import TestCase
from django.urls import reverse
import answer.database_manager as script
from .models import Product

test_database_manager = script.Database_manager()


class IndexPageTestCase(TestCase):
    def test_index_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)


class SearchPageTestCase(TestCase):
    def test_search_page(self):
        response = self.client.get(reverse('search-products'))
        self.assertEqual(response.status_code, 200)


class TestDatabase_manager(TestCase):
    query = "lait chocolat"
    query_complete = "Bâtonnets sablés chocolat au lait"
    product_name = "Bâtonnets sablés chocolat au lait"
    product_category ='Snacks'
    product_id = 1295
    product_link = 'https://fr.openfoodfacts.org/produit/3350033111868/batonnets-sables-chocolat-au-lait-monoprix-gourmet'
    product_nutriscore = 'e'
    product_picture = 'https://static.openfoodfacts.org/images/products/335/003/311/1868/front_fr.27.400.jpg'
    product_elements = product_name, product_picture, product_nutriscore, product_category, product_link, product_id
    best_ratio_list = 	['Bâtonnets sablés chocolat au lait','Gâteau au chocolat noir','Petit beurre tablette chocolat au lait','Bâtonnets de chocolat']
    better_nutriscore_list = ['a', 'b', 'c', 'd', 'e']
    product_ratio_list = ['Gâteau au chocolat noir','Chocolat Lait','Bâtonnets de chocolat','Croustifondante Chocolat','Ferme & Fondant Chocolat',
     'Gaufrettes choco','Delichoc','Délichoc','Délichoc sablé','Savane Le Classique Chocolat','Biscuits nappés chocolat noir','BN goût chocolat',
     'Biscuit Avoine et Chocolat','Fitness Chocolat Noir','Kinder chocolat mini eggs','Chocolat Happy','Kinder Chocolat',
     'Bitter Schokolade','Petit-beurre Chocolat Noir','Biscuit choco fondant noir','Biscuit Lait Chocolat','Finest dark chocolate',
     'Lindt Chocoletti au lait','Kinder Pingui Chocolat','pâturages Soja chocolat','Soja à boire chocolat','Boisson soja au chocolat',
     'Haricots plats','Pains au chocolat pur beurre,','Pains au chocolat pur beurre','Pain au Chocolat','croissant chocolat',
     'Brioche tranchée pépites chocolat','Pitchs au chocolat au lait','Beignets au Chocolat','8 pitch beignets goût chocolat',
     'Céréales Crica chocolat 400 g','Muesli croustillant au chocolat','Muesli granola figues et chocolat','Boules enrobées au chocolat',
     'Pétales de blé chocolat','Boules de céréales chocolat','Céréales pétales blé chocolat','Tablette de chocolat noir','Eclair chocolat surgele',
     'Mini Cakes Tout Chocolat','Gaufrettes fourrées chocolat','Beignet au Chocolat','Crème dessert chocolat','Dessert lacté gélifié au chocolat',
     'Crème dessert au chocolat','Mousse au chocolat noir','Kinder chocolat','½ Mètre Kinder chocolat','Crème glacée menthe chocolat','Coupes liégeoises chocolat',
     'Dessert glacé 3 cioccolato','Cônes chocolat','Cônes menthe chocolat','Glace café avec grains de chocolat','Feuilleté glacé menthe chocolat',
     'Croquant aux 2 chocolats','Petits cônes vanille-chocolat','Bâtonnets vanille et chocolat','Crème glacée 3 chocolats','Lait ribot',
     'Lait UHT arôme chocolat','Mi-cho-ko au chocolat noir','Gélifiés crocodile','Boule coco','Royal biscuit goût tout chocolat',
     'Batonnets au chocolat au lait','Stikéo batonnets chocolat noir','Stikéo batonnets chocolat lait','Biscuits pépites chocolat',
     'Spéculoos aux 3 chocolats',"P'tit déj pépites de chocolat",'Sprits au chocolat au lait','Cookies quinoa pépites chocolat','Bâtonnets folie de chocolat']


    def test_find_similar_name(self):
        assert script.Database_manager.find_similar_name(test_database_manager, self.query) == self.product_ratio_list

    def test_multiple_product_name(self):
        pass

    def test_product_chosen(self):
        assert script.Database_manager.product_chosen(test_database_manager,
                                                      self.query_complete) == self.product_elements

    def get_same_names(self):
        assert script.Database_manager.get_same_names(test_database_manager, self.query_complete,
                                                      self.product_category) == self.best_ratio_list

    def get_better_nutriscore(self):
        assert script.Database_manager.get_better_nutriscore(test_database_manager,
                                                             self.product_nutriscore) == self.better_nutriscore_list

    """def extract_products_for_replace(self, better_nutriscores_list, product_category, best_ratio_list, product_link):
        assert script.Database_manager.get_better_nutriscore(test_database_manager,
                                                             self.product_nutriscore) == self.better_nutriscore_list"""
