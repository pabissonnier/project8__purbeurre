from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

from answer.database_manager import Database_manager
from .models import UserList, User
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
    if request.method == 'POST':
        query = request.POST.get('fav-btn')
        products_datas = Database_manager()
        Database_manager.product_to_userlist(products_datas, query)
