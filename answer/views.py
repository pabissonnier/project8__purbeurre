# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.core.exceptions import MultipleObjectsReturned
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
        products_all_list = Product.objects.all()
        paginator = Paginator(products_all_list, 10)
        page = request.GET.get('page')
        products_all = paginator.get_page(page)
        title = "Résultats pour la recherche : '%s'" % query
        context = {
            'products_all': products_all,
            'title': title,
        }
        return render(request, 'answer/search.html', context)
    else:
        products_list = Product.objects.filter(name__icontains=query)
        paginator = Paginator(products_list, 10)
        page = request.GET.get('page')
        products = paginator.get_page(page)
        if not products_list.exists():
            message = "Aucun produit trouvé"
        title = "Résultats pour la recherche : '%s'" % query
        context = {
            'products': products,
            'title': title,
        }
        return render(request, 'answer/search.html', context)


def app(request):
    query = request.GET.get('app-query')
    products_datas = Database_manager()
    if not query:
        products_list = Product.objects.all().order_by('name')
        title = "Aucun produit n'a été renseigné, choisissez dans la liste de produits ou recherchez un produit"
        context = {
            'title': title,
            'products_list': products_list,
        }
        return render(request, 'answer/results.html', context)
    else:
        try:
            products = Product.objects.filter(name=query)
            if not products.exists():
                products_names = Database_manager.find_product_name(products_datas, query)
                url_names_dict = Database_manager.product_name_to_url(products_datas, products_names)
                title = "Aucun produit pour : '%s', choisissez un produit dans la liste ci-dessous" % query
                context = {
                    'title': title,
                    'products_url_and_names': url_names_dict,
                }
                return render(request, 'answer/list.html', context)

            product_name, product_picture, product_nutriscore, product_category = Database_manager.product_chosen(products_datas, query)
            better_nutriscore = Database_manager.get_better_nutriscore(products_datas, product_nutriscore)
            best_ratio_list = Database_manager.get_same_names(products_datas, product_name, product_category)
            better_products = Database_manager.extract_products_for_replace(products_datas, better_nutriscore, product_category,
                                                                            best_ratio_list)
            title = "Voici de meilleurs produits pour remplacer : '%s'" % query
            context = {
                'title': title,
                'name': product_name,
                'picture': product_picture,
                'nutriscore': product_nutriscore,
                'better_products': better_products,
            }
            return render(request, 'answer/results.html', context)
        except MultipleObjectsReturned:
            element = Database_manager.multiple_product_name(products_datas, query)
            title = "Plusieurs produits pour : '%s', choisissez un produit dans la liste ci-dessous" % query
            context = {
                'title': title,
                'element': element
            }
            return render(request, 'answer/list.html', context)


def app_link(request, product_name):
    products_datas = Database_manager()
    product_dict = Product.objects.filter(name=product_name)
    for key, value in product_dict:
        product = value['product_name']
        product_name, product_picture, product_nutriscore, product_category = Database_manager.product_chosen(
            products_datas, product)
        better_nutriscore = Database_manager.get_better_nutriscore(products_datas, product_nutriscore)
        best_ratio_list = Database_manager.get_same_names(products_datas, product_name, product_category)
        better_products = Database_manager.extract_products_for_replace(products_datas, better_nutriscore, product_category,
                                                                        best_ratio_list)
        title = "Voici de meilleurs produits pour remplacer : '%s'" % product_name
        context = {
            'title': title,
            'name': product_name,
            'picture': product_picture,
            'nutriscore': product_nutriscore,
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
