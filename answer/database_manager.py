# -*- coding: utf-8 -*-

from answer.models import Product
from difflib import SequenceMatcher


class Database_manager:

    def find_similar_name(self, query):
        """ If app-query doesn't exist and is more than one string, find similar product names in the db"""
        products_ratio_list = []
        products_list = Product.objects.all().values('name')
        for element in products_list:
            for key, value in element.items():
                product_score = SequenceMatcher(None, query, value).ratio()
                if product_score > 0.5:
                    products_ratio_list.append(value)
        return products_ratio_list

    def multiple_product_name(self, query):
        """ If many products with similar name """
        products_same_name = []
        products_list = Product.objects.get(name=query)
        pass

    def product_chosen(self, query):
        """ Display elements of the product chosen (name, picture, nutriscore)"""
        product = Product.objects.get(name=query)
        return product.name, product.picture, product.nutriscore, product.category, product.link, product.id

    def get_same_names(self, product_name, product_category):
        """ Get similar product names """
        products_ratio_list = []
        products_list = Product.objects.filter(category=product_category).values('name')
        for element in products_list:
            for key, value in element.items():
                product_score = SequenceMatcher(None, product_name, value).ratio()
                if product_score > 0.5:
                    products_ratio_list.append(value)
        return products_ratio_list

    def get_better_nutriscore(self, product_nutriscore):
        """ Gets better nutriscore, if 'c' = 'a', 'b', if doesn't exist higher, take the same NC"""
        nutriscore_list = ['a', 'b', 'c', 'd', 'e']
        better_nutriscores_list = []
        if product_nutriscore in nutriscore_list:
            nutriscore_position = nutriscore_list.index(product_nutriscore) + 1
            nutriscores_wanted = nutriscore_list[:nutriscore_position]
            for elements in nutriscores_wanted:
                better_nutriscores_list.append(elements)
        elif product_nutriscore == nutriscore_list[0]:
            nutriscores_wanted = nutriscore_list[0]
            better_nutriscores_list.append(nutriscores_wanted)
        return better_nutriscores_list

    def extract_products_for_replace(self, better_nutriscores_list, product_category, best_ratio_list, product_link):
        """ Takes products with same category and higher nutriscore"""
        better_nutriscores_list = Product.objects.filter(category=product_category).filter(name__in=best_ratio_list).\
            filter(nutriscore__in=better_nutriscores_list).exclude(link=product_link)
        return better_nutriscores_list

    def product_to_userlist(self, product):
        """ To put the product into the userlist table"""
        insertion_datas = Product(name=product.name, category=product.category,
                                  ingredients=product.ingredients, nutriscore=product.nutriscore,
                                  picture=product.picture, shops=product.shops, link=product.link)
        data_inside = Product.objects.get(link=product.link)
        if not data_inside:
            insertion_datas.save()
        else:
            pass


