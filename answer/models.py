# -*- coding: utf-8 -*-

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from difflib import SequenceMatcher


class Product(models.Model):
    name = models.CharField(max_length=1000, null=True)
    category = models.CharField(max_length=1000, null=True)
    nutriscore = models.CharField(max_length=1, null=True)
    ingredients = models.CharField(max_length=5000, null=True)
    shops = models.CharField(max_length=1000, null=True)
    link = models.CharField(max_length=1000, null=True, unique=True)
    picture = models.URLField()
    favorites = models.ManyToManyField(User, related_name='favorite', blank=True)
    labels = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("application")

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
        products_list = Product.objects.filter(name__iexact=query)
        return products_list

    def product_chosen(self, query):
        """ Display elements of the product chosen"""
        product = Product.objects.get(name__iexact=query)
        return product.name, product.picture, product.nutriscore, product.category, product.link, product.id

    def product_chosen_sim(self, query):
        """ Display elements of the product chosen"""
        product = Product.objects.get(id=query)
        return product.name, product.picture, product.nutriscore, product.category, product.link, product.id

    def get_same_names(self, product_name, product_category):
        """ Get similar product names in the same category """
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
        better_products = Product.objects.filter(category=product_category).filter(name__in=best_ratio_list).\
            filter(nutriscore__in=better_nutriscores_list).exclude(link=product_link).order_by('name')
        return better_products

    def bio_or_not(self, product):
        """ Checks if the product is BIO or not for display """
        if "Bio" in product.labels:
            is_bio = True
        else:
            is_bio = False
        return is_bio
