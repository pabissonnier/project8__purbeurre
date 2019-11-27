# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from users import views as user_views
from answer import views as answer_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', answer_views.index, name='home'),
    url(r'^answer/', answer_views.app, name='application'),
    url(r'^answer_/', answer_views.app_sim, name='application_sim'),
    url(r'^(?P<product_id>[0-9]+)/$', answer_views.detail, name='detail'),
    url(r'^favorite_product/$', user_views.favs, name='favorite_product'),
    url(r'^defavorite_product/$', user_views.defavs, name='defavorite_product'),
    url(r'^bio_product/$', answer_views.bio_filter, name='bio_filter'),
    url(r'^search/$', answer_views.search, name='search-products'),
    url(r'^admin/', admin.site.urls),
    url(r'^register/', user_views.register, name='register'),
    url(r'^login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name='login'),
    url(r'^logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name='logout'),
    url(r'^profile/', user_views.profile, name='profile'),
    url(r'^favs/', user_views.show_favs, name='show_favs'),
    url(r'^contact/', user_views.contact, name='contact'),
    url(r'^legalmentions/', user_views.mentions, name='mentions'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

