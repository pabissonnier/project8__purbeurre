from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from answer.database_manager import Database_manager
from .models import User
from answer.models import Product


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Compte créé avec succès, vous pouvez maintenant vous logger')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required()
def profile(request):
    return render(request, 'users/profile.html')


@login_required()
def favs(request):
    """ Add product to user list"""
    product = get_object_or_404(Product, id=request.POST.get('fav-btn'))
    product.favorites.add(request.user)
    return HttpResponseRedirect("")

    """product = get_object_or_404(Product, id=id)
    if product.favorites.filter(id=request.user.id).exists():
        product.favorites.remove(request.user)
    else:
        product.favorites.add(request.user)
    return HttpResponseRedirect("")"""



    """product = request.GET['fav-btn']
    products_datas = Database_manager()
    Database_manager.product_to_userlist(products_datas, product)"""

