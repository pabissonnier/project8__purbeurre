# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import MultipleObjectsReturned
from django.core.paginator import Paginator

from .models import Product


def index(request):
    return render(request, 'answer/index.html')


def search(request):
    query = request.GET.get('query')
    global message
    if not query:
        products_all_list = Product.objects.all().order_by('name')
        paginator = Paginator(products_all_list, 9)
        page = request.GET.get('page')
        products_all = paginator.get_page(page)
        title = "Résultats pour la recherche : '%s'" % query
        context = {
            'products': products_all,
            'title': title,
            'query': query,
        }
        return render(request, 'answer/search.html', context)
    else:
        products_list = Product.objects.filter(name__icontains=query).order_by('name')
        paginator = Paginator(products_list, 9)
        page = request.GET.get('page')
        products = paginator.get_page(page)
        if not products_list.exists():
            message = "Aucun produit trouvé"
        title = "Résultats pour la recherche : '%s'" % query
        context = {
            'products': products,
            'title': title,
            'query': query
        }
    return render(request, 'answer/search.html', context)


def app(request):
    query = request.GET.get('app-query')
    products_datas = Product()

    if not query:
        products_list = Product.objects.all().order_by('name')
        paginator = Paginator(products_list, 9)
        page = request.GET.get('page')
        products_all = paginator.get_page(page)
        title = "Aucun produit n'a été renseigné, choisissez dans la liste de produits ou recherchez un produit"
        context = {
            'title': title,
            'products': products_all,
            'query': query,
        }
        return render(request, 'answer/list.html', context)
    else:
        try:
            products = Product.objects.filter(name__iexact=query)

            if not products.exists():
                space = ' '
                if space in query:
                    products_ratio_list = Product.find_similar_name(products_datas, query)
                    products = Product.objects.filter(name__in=products_ratio_list).order_by('name')
                    paginator = Paginator(products, 9)
                    page = request.GET.get('page')
                    products_all = paginator.get_page(page)
                    title = "Aucun produit pour : '%s', choisissez un produit dans la liste ci-dessous" % query
                    context = {
                        'title': title,
                        'products': products_all,
                        'query': query,
                    }
                    return render(request, 'answer/list.html', context)
                else:
                    products = Product.objects.filter(name__icontains=query).order_by('name')
                    paginator = Paginator(products, 9)
                    page = request.GET.get('page')
                    products_all = paginator.get_page(page)
                    title = "Plusieurs produits contiennent : '%s', choisissez un produit dans la liste ci-dessous" % query
                    context = {
                        'title': title,
                        'products': products_all,
                        'query': query,
                    }
                    return render(request, 'answer/list.html', context)

            product_name, product_picture, product_nutriscore, product_category, product_link, product_id = \
                Product.product_chosen(products_datas, query)

            better_nutriscore = Product.get_better_nutriscore(products_datas, product_nutriscore)
            best_ratio_list = Product.get_same_names(products_datas, product_name, product_category)
            better_products = Product.extract_products_for_replace(products_datas, better_nutriscore, product_category,
                                                                            best_ratio_list, product_link)

            title = "Voici de meilleurs produits pour remplacer : '%s'" % query
            if not better_products:
                title = "Désolé, nous n'avons pas de meilleurs produits pour remplacer : '%s'" % query
            context = {
                'title': title,
                'better_products': better_products,
                'query': query,
            }
            return render(request, 'answer/results.html', context)

        except MultipleObjectsReturned:
            products = Product.multiple_product_name(products_datas, query)
            title = "Plusieurs produits pour : '%s', choisissez un produit dans la liste ci-dessous" % query
            context = {
                'title': title,
                'products': products,
                'query': query,
            }
            return render(request, 'answer/simlist.html', context)


def app_sim(request):
    query = request.GET.get('app-query-sim')
    products_datas = Product()

    product = Product.objects.get(id=query)

    better_nutriscore = Product.get_better_nutriscore(products_datas, product.nutriscore)
    best_ratio_list = Product.get_same_names(products_datas, product.name, product.category)
    better_products = Product.extract_products_for_replace(products_datas, better_nutriscore, product.category,
                                                                    best_ratio_list, product.link)

    title = "Voici de meilleurs produits pour remplacer : '%s'" % product.name
    if not better_products:
        title = "Désolé, nous n'avons pas de meilleurs produits pour remplacer : '%s'" % product.name
    context = {
        'title': title,
        'better_products': better_products,
        'query': query,
    }
    return render(request, 'answer/results.html', context)


def detail(request, product_id):
    """ Display details for the product clicked"""
    products_datas = Product()
    product = get_object_or_404(Product, pk=product_id)
    is_bio = Product.bio_or_not(products_datas, product)
    context = {
        'name': product.name,
        'picture': product.picture,
        'nutriscore': product.nutriscore,
        'ingredients': product.ingredients,
        'shops': product.shops,
        'link': product.link,
        'labels' : product.labels,
        'product': product,
        'is_bio': is_bio
    }
    return render(request, 'answer/detail.html', context)
