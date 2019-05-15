from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Products, User, UserList


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
    title = "Voici de meilleurs produits pour : '%s'" % query
    context = {
        'products': products,
        'title': title,
    }
    return HttpResponse(render(request, 'answer/results.html', context))
