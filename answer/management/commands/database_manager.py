from answer.models import Products
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):

    def product_chosen(self, product_name):
        """ Display elements of the product chosen (name, picture, nutriscore)"""
        product = Products.objects.get(name=product_name)
        product_picture = product.picture
        product_nutriscore = product.nutriscore
        return product_name, product_picture, product_nutriscore

