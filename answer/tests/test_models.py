from django.test import TestCase
from django.urls import reverse
import answer.database_manager as script
from answer.models import Product

test_database_manager = script.Database_manager()





"""class TestDatabase_manager(TestCase):
    query = "lait chocolat"
    query_complete = "Bâtonnets sablés chocolat au lait"
    query_complete_case = "bâtonnets Sablés Chocolat Au Lait"
    best_ratio_list = 	['Bâtonnets sablés chocolat au lait','Gâteau au chocolat noir','Petit beurre tablette chocolat au lait','Bâtonnets de chocolat']
    better_nutriscore_list = ['a', 'b', 'c', 'd', 'e']
    product_ratio_list = [ 'Finest dark chocolate', 'Lindt Chocoletti au lait', 'Kinder Pingui Chocolat', 'pâturages Soja chocolat', 'Soja à boire chocolat', 'Boisson soja au chocolat', 'Haricots plats', 'Pains au chocolat pur beurre,', 'Pains au chocolat pur beurre', 'Pain au Chocolat', 'croissant chocolat', 'Brioche tranchée pépites chocolat', 'Pitchs au chocolat au lait', 'Beignets au Chocolat', '8 pitch beignets goût chocolat', 'Céréales Crica chocolat 400 g', 'Muesli croustillant au chocolat', 'Muesli granola figues et chocolat', 'Boules enrobées au chocolat', 'Pétales de blé chocolat', 'Boules de céréales chocolat', 'Céréales pétales blé chocolat', 'Tablette de chocolat noir', 'Eclair chocolat surgele', 'Mini Cakes Tout Chocolat', 'Gaufrettes fourrées chocolat', 'Beignet au Chocolat', 'Crème dessert chocolat', 'Dessert lacté gélifié au chocolat', 'Crème dessert au chocolat', 'Mousse au chocolat noir', 'Kinder chocolat', '½ Mètre Kinder chocolat', 'Crème glacée menthe chocolat', 'Coupes liégeoises chocolat', 'Dessert glacé 3 cioccolato', 'Cônes chocolat', 'Cônes menthe chocolat', 'Glace café avec grains de chocolat', 'Feuilleté glacé menthe chocolat', 'Croquant aux 2 chocolats', 'Petits cônes vanille-chocolat', 'Bâtonnets vanille et chocolat', 'Crème glacée 3 chocolats', 'Lait ribot', 'Lait UHT arôme chocolat', 'Mi-cho-ko au chocolat noir', 'Gélifiés crocodile', 'Boule coco', 'Royal biscuit goût tout chocolat', 'Batonnets au chocolat au lait', 'Stikéo batonnets chocolat noir', 'Stikéo batonnets chocolat lait', 'Biscuits pépites chocolat', 'Spéculoos aux 3 chocolats', 'P''tit déj pépites de chocolat', 'Sprits au chocolat au lait', 'Cookies quinoa pépites chocolat', 'Bâtonnets folie de chocolat', 'Pépites aux éclats de chocolat', 'La madeleine coque chocolat', 'Liégeois saveur chocolat', 'Galletas de chocolate', 'Nocciolata', 'Weetabix Minis Chocolate', 'Riz au lait au chocolat', 'Goûter pépites de chocolat', 'Prince multicéréales goût chocolat', 'Pépites chocolat noir', 'Chocolat noir', 'Petits muffins au chocolat', 'Oil Cauvin Coconut', 'Petit beurre chocolat lait', 'pain au chocolat', 'Pains au chocolat Bio', 'Pains au lait barre chocolat', 'Pains au chocolat', 'Riz soufflé au chocolat', 'Muesli au Chocolat', 'Goûter laitier au Chocolat', 'Petits pots de creme chocolat', 'Amandes chocolatées', 'Candy''Up Chocolaté', 'Biscuits meringués au chocolat', 'Petit beurre au chocolat noir', 'Barquettes chocolat noisette', 'Chocolat', 'Miletto gaufrettes chocolat', 'Dessert végétal chocolat', 'St Hubert Végétal Bio chocolat', 'Lait de coco', 'Biscuit Sésame chocolat', 'Chocolat blanc', 'Moelleux au Chocolat', 'Mini fourrés cœur chocolat', 'Moelleux aux pépites de chocolat', 'Danette chocolat et lait', '10 pains au chocolat', 'Muesli croustillant chocolat', 'Fitness cup choco lait', 'Extrême Chocolat', 'Haribo croco', 'Petit Beurre Chocolat', 'Coup double chocolat', 'Tablette de chocolat au lait', 'Pépites de chocolat au lait', 'Chocolat lait', 'Triple goût chocolat', 'Belgian Chocolat', 'Crèmeuh chocolat', 'Noix de Coco et Chocolat', 'Bâtonnets chocolat', 'Cônes vanille chocolat,', 'Creme glace chocolat', 'Glace boni au chocolat', 'Bâtonnet Glacé Chocolat', 'Porridge chocolat', 'Pépites Croustillantes au chocolat', 'Croustillant aux 2 chocolats', 'Extra chocolat noir', 'Krounchy too chocolat', 'Cruesli chocolat noir', 'Croustillant chocolat sans gluten', 'Farmer Croc Chocolat', 'Pitch Pépites de Chocolat', 'Pitch choco barre', 'Pitch Chocolat au Lait', 'Bizz Maxi choco', 'Saveur chocolat au lait', 'Damhert Tag Chocopasta', 'Tartelettes chocolat noir', 'Tartelettes au chocolat noir', 'Tarte Chocolat Noisette', 'Mini gateaux fourré chocolat', 'Mini moelleux chocolat', 'Mini moelleux aux pépites de chocolat', 'Gâteau au Chocolat', 'Cakes aux pépites de chocolat', 'tendre lapin chocolat', 'Mini brownies pépites chocolat', 'Moelleux au chocolat', 'Petits marbrés au chocolat', 'Mini Moelleux au Chocolat', 'Brownie chocolat noisettes', 'Madeleines aux pépites de chocolat', 'Madeleines pépites de chocolat', 'Sablés tout chocolat', 'Biscuits Fourrés Goût chocolat', 'Sablé fourré chocolat', 'Biscuits fourrés chocolat lait', 'Sprits chocolat au lait', 'Lait de Coco', 'Alpro lait de coco', 'Lait d''Amande Chocolat', 'Boisson au riz. Chocolat', 'Lait De Coco Nature', 'Gauffres chovolat', 'barre protéinée au chocolat']

    def setup(self):
        Product.objects.create(name="Bâtonnets sablés chocolat au lait", id=1295, nutriscore='e',
                               link='https://fr.openfoodfacts.org/produit/3350033111868/batonnets-sables-chocolat-au-lait-monoprix-gourmet',
                               category='Snacks', picture='https://static.openfoodfacts.org/images/products/335/003/311/1868/front_fr.27.400.jpg')

        Product.objects.create(name='Gâteau au chocolat noir', nutriscore='d', category='Snacks')
        Product.objects.create(name='Chocolat Lait', nutriscore='e', category='Snacks')
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
        names = script.Database_manager.find_similar_name(test_database_manager, self.query)
        self.assertEqual(names, self.product_ratio_list)

    def test_multiple_product_name(self):
        name = script.Database_manager.multiple_product_name(test_database_manager, self.query_complete_case)
        self.assertEqual(name, self.query_complete)

    def test_product_chosen(self):
        product_chosen = script.Database_manager.product_chosen(test_database_manager,
                                                      self.query_complete)
        self.assertEqual(product_chosen, self.product_elements)

    def test_product_chosen_sim(self):
        product_chosen = script.Database_manager.product_chosen_sim(test_database_manager,
                                                      self.product_id)
        self.assertEqual(product_chosen, self.product_elements)

    def test_get_same_names(self):
        same_names = script.Database_manager.get_same_names(test_database_manager, self.query_complete,
                                                            self.product_category)
        self.assertEqual(same_names, self.best_ratio_list)

    def test_get_better_nutriscore(self):
        better_nutriscore = script.Database_manager.get_better_nutriscore(test_database_manager, self.product_nutriscore)
        self.assertEqual(better_nutriscore, self.better_nutriscore_list)

    def test_extract_products_for_replace(self):
        products_for_replace = script.Database_manager.extract_products_for_replace(test_database_manager,
                                                             self.better_nutriscore_list, self.product_category,
                                                                                self.best_ratio_list, self.product_link)
        self.assertEqual(products_for_replace, self.best_ratio_list)"""

