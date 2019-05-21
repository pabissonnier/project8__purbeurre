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
    if not query:
        products = Products.objects.all()
    else:
        products = Products.objects.filter(name__icontains=query)
        if not products.exists():
            message = "Aucun produit trouvé"
    title = "Résultats pour la recherche : '%s'" % query
    context = {
        'products': products,
        'title': title
    }
    return HttpResponse(render(request, 'answer/search.html', context))


def app(request):
    query = request.GET.get('app-query')
    if not query:
        products = Products.objects.all()
    else:
        products = Products.objects.filter(name__icontains=query)
        if not products.exists():
            message = "Aucun produit trouvé"
    products_datas = Database_manager()
    product_name, product_picture, product_nutriscore = Database_manager.product_chosen(products_datas, query)
    title = "Voici de meilleurs produits pour remplacer : '%s'" % product_name
    context = {
        'title': title,
        'name': product_name,
        'picture': product_picture,
        'nutriscore': product_nutriscore,
    }
    return HttpResponse(render(request, 'answer/results.html', context))

