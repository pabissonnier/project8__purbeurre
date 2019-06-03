from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

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
    is_liked = False
    if product.favorites.filter(id=request.user.id).exists():
        product.favorites.remove(request.user)
        is_liked = False
    else:
        product.favorites.add(request.user)
        is_liked = True
    return HttpResponseRedirect(product.get_absolute_url())

@login_required()
def show_favs(request):
    products_list = Product.objects.filter(favorites=request.user).order_by('name')
    title = "Voici vos favoris"
    context = {
        'products_list': products_list,
        'title': title,
    }
    return render(request, 'users/favs.html', context)
