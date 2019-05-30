# -*- coding: utf-8 -*-

from answer.models import Product
from users.models import User, UserList

from difflib import SequenceMatcher


class Database_manager:

    def find_product_name(self, query):
        products_ratio_list = []
        products_list = Product.objects.all().values('name')
        for element in products_list:
            for key, value in element.items():
                product_score = SequenceMatcher(None, query, value).ratio()
                if product_score > 0.5:
                    products_ratio_list.append(value)
        return products_ratio_list

    def query_in_name(self, query):
        product_query_name = []
        products_list = Product.objects.all().values('name').order_by('name')
        for element in products_list:
            for key, value in element.items():
                if query in value:
                    product_query_name.append(value)
        return product_query_name

    def multiple_product_name(self, query):
        """ If many products with similar name """
        products_same_name = []
        products_list = Product.objects.get(name=query)
        pass

    def product_name_to_url(self, product_list):
        """ Convert product name to querystyle """
        product_url_list = []
        for product in product_list:
            product_url_dict = {}
            product_name_url = product.replace("'", '%27')
            product_name_url = product_name_url.replace(' ', '+')
            product_url_dict[product] = product_name_url
            product_url_list.append(product_url_dict)
        return product_url_list

    def product_chosen(self, query):
        """ Display elements of the product chosen (name, picture, nutriscore)"""
        product = Product.objects.get(name=query)
        product_name = product.name
        product_picture = product.picture
        product_nutriscore = product.nutriscore
        product_category = product.category
        return product_name, product_picture, product_nutriscore, product_category

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

    def extract_products_for_replace(self, better_nutriscores_list, product_category, best_ratio_list):
        """ Takes products with same category and higher nutriscore"""
        better_nutriscores_list = Product.objects.filter(category=product_category).filter(name__in=best_ratio_list).\
            filter(nutriscore__in=better_nutriscores_list)
        return better_nutriscores_list

    def product_to_userlist(self, query):
        """ To put the product into the userlist table"""
        product = Product.objects.get(query)
        product_name = product.name
        product_picture = product.picture
        product_nutriscore = product.nutriscore
        product_category = product.category
        product_shops = product.shops
        product_ingredients = product.ingredients
        product_link = product.link
        insertion_datas = UserList(name=product_name, category=product_category,
                                  ingredients=product_ingredients, nutriscore=product_nutriscore,
                                  picture=product_picture, shops=product_shops, link=product_link)
        data_inside = UserList.objects.filter(link=product_link)
        if not data_inside:
            insertion_datas.save()
        else:
            pass


