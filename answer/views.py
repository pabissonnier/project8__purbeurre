# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .database_manager import Database_manager
from django.core.paginator import Paginator

from .models import Product


def index(request):
    return render(request, 'answer/index.html')


def search(request):
    query = request.GET.get('query')
    global message
    if not query:
        products = Product.objects.all()
    else:
        products = Product.objects.filter(name__icontains=query)
        if not products.exists():
            message = "Aucun produit trouvé"
    title = "Résultats pour la recherche : '%s'" % query
    context = {
        'products': products,
        'title': title,
    }
    return render(request, 'answer/search.html', context)


def app(request):
    query = request.GET.get('app-query')
    if not query:
        products_list = Product.objects.all()
        paginator = Paginator(products_list, 5)
        page = request.Get.get('page')
        products = paginator.page(page)
    else:
        products = Product.objects.filter(name__icontains=query)
        if not products.exists():
            products = Product.objects.all() # remplacer par template contenant les produits qui peuvent s'apparenter

    products_datas = Database_manager()
    product_name, product_picture, product_nutriscore, product_category = Database_manager.product_chosen(products_datas, query)
    better_nutriscore = Database_manager.get_better_nutriscore(products_datas, product_nutriscore)
    better_products = Database_manager.extract_products_for_replace(products_datas, better_nutriscore, product_category)
    title = "Voici de meilleurs produits pour remplacer : '%s'" % query
    context = {
        'title': title,
        'name': product_name,
        'picture': product_picture,
        'nutriscore': product_nutriscore,
        'products': products,
        'better_products': better_products,
    }
    return render(request, 'answer/results.html', context)


def detail(request, product_id):
    """ Display details for the product clicked"""
    product = Product.objects.get(pk=product_id)
    context = {
        'name': product.name,
        'picture': product.picture,
        'nutriscore': product.nutriscore,
        'ingredients': product.ingredients,
        'shops': product.shops,
        'link': product.link,
        'album_id': product.id
    }
    return render(request, 'answer/detail.html', context)
