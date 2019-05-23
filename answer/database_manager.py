# -*- coding: utf-8 -*-

from answer.models import Product

class Database_manager:

    def product_chosen(self, query):
        """ Display elements of the product chosen (name, picture, nutriscore)"""
        product = Product.objects.get(name__icontains=query)
        product_name = product.name
        product_picture = product.picture
        product_nutriscore = product.nutriscore
        return product_name, product_picture, product_nutriscore


