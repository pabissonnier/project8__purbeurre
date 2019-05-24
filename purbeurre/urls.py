# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from users import views as user_views
from answer import views as answer_views

urlpatterns = [
    url(r'^$', answer_views.index, name='home'),
    url(r'^answer/', answer_views.app, name='application'),
    url(r'^(?P<product_id>[0-9]+)/$', answer_views.detail, name='detail'),
    url(r'^search/$', answer_views.search, name='search-products'),
    url(r'^admin/', admin.site.urls),
    url(r'^register/', user_views.register, name='register'),
    url(r'^login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name='login'),
    url(r'^logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name='logout'),

]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
