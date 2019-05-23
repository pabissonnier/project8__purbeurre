# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .database_manager import Database_manager

from .models import Product, UserList


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
    return HttpResponse(render(request, 'answer/search.html', context))


def app(request):
    query = request.GET.get('app-query')
    if not query:
        products = Product.objects.all()
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
        'better_products': better_products
    }
    return HttpResponse(render(request, 'answer/results.html', context))


def detail(request):
    pass
