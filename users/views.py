from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from answer.models import Product
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            save_it = form.save()

            subject = "Merci pour votre inscription !"
            message = 'Hello {0},\n\n' \
                      'Vous pouvez désormais ajouter des produits à votre liste de favoris...\n\n'\
                      'A bientôt chez Purbeurre'.format(save_it.username)
            from_email = settings.EMAIL_HOST_USER
            to_list = [save_it.email, settings.EMAIL_HOST_USER]
            send_mail(subject, message, from_email, to_list, fail_silently=True)

            messages.success(request, f'Compte créé avec succès, vous pouvez maintenant vous logger')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required()
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Compte mis à jour !')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)


@login_required()
def favs(request):
    """ Add product to user list"""
    product = get_object_or_404(Product, id=request.POST.get('fav-btn'))
    product.favorites.add(request.user)
    return redirect(request.META['HTTP_REFERER'])


@login_required()
def defavs(request):
    """ Remove product from user list"""
    product = get_object_or_404(Product, id=request.POST.get('defav-btn'))
    product.favorites.remove(request.user)
    return redirect(request.META['HTTP_REFERER'])


@login_required()
def show_favs(request):
    products_list = Product.objects.filter(favorites=request.user).order_by('name')
    title = "Vos favoris"
    context = {
        'products_list': products_list,
        'title': title,
    }
    return render(request, 'users/favs.html', context)


def contact(request):
    return render(request, 'users/contact.html')


def mentions(request):
    return render(request, 'users/mentions.html')
