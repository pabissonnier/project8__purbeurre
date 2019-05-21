# -*- coding: utf-8 -*-

from answer.models import Product

class Database_manager:

    def product_chosen(self, product_name):
        """ Display elements of the product chosen (name, picture, nutriscore)"""
        product = Products.objects.get(name=product_name)
        product_picture = product.picture
        product_nutriscore = product.nutriscore
        return product_name, product_picture, product_nutriscore

    def better_nutriscore(self, nutriscore):
        """ Gets 3 to 5 better products """
        nutriscore_list = ['A', 'B', 'C', 'D', 'E']
        better_nutriscores_list = []
        nutriscore_product = nutriscore.upper()
        if nutriscore_product in nutriscore_list:
            nutriscore_position = nutriscore_list.index(nutriscore_product) + 1
            nutriscores_wanted = nutriscore_list[:nutriscore_position]
            for elements in nutriscores_wanted:
                better_nutriscores_list.append(elements)
        elif nutriscore_product == nutriscore_list[0]:
            nutriscores_wanted = nutriscore_list[0]
            better_nutriscores_list.append(nutriscores_wanted)
        return better_nutriscores_list

    def extract_products_for_replace(self, category, better_nutriscores_list):
        """ Takes products with same category and higher nutriscore"""
        products_for_replace = []

        for nutriscore in better_nutriscores_list:
            data = (category, nutriscore)
            query = "SELECT name, nutriscore, link FROM product WHERE nom_category = %s AND nutriscore = %s"
            cursor.execute(query, data)

            products_for_replace.append(products_with_better_nutriscore)

        return products_for_replace
