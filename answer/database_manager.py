# -*- coding: utf-8 -*-

from answer.models import Product

class Database_manager:

    def product_chosen(self, query):
        """ Display elements of the product chosen (name, picture, nutriscore)"""
        product = Product.objects.get(name__icontains=query)
        product_name = product.name
        product_picture = product.picture
        product_nutriscore = product.nutriscore
        product_category = product.category
        return product_name, product_picture, product_nutriscore, product_category

    def get_better_nutriscore(self, product_nutriscore):
        nutriscore_list = ['a', 'b', 'c', 'd', 'e']
        better_nutriscores_list = []
        if product_nutriscore in nutriscore_list:
            nutriscore_position = nutriscore_list.index(product_nutriscore)
            nutriscores_wanted = nutriscore_list[:nutriscore_position]
            for elements in nutriscores_wanted:
                better_nutriscores_list.append(elements)
        elif product_nutriscore == nutriscore_list[0]:
            nutriscores_wanted = nutriscore_list[0]
            better_nutriscores_list.append(nutriscores_wanted)
        return better_nutriscores_list

    def extract_products_for_replace(self, better_nutriscores_list, product_category):
        """ Takes products with same category and higher nutriscore"""

        better_nutriscores_list = Product.objects.filter(category=product_category).filter(nutriscore__in= better_nutriscores_list)
        return better_nutriscores_list
