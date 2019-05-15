from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
# from user import views as user_views
from answer import views as answer_views

urlpatterns = [
    url(r'^$', answer_views.index, name='home'),
    url(r'^answer/', answer_views.app, name='application'),
    # url(r'^products/', include('products.urls')),
    url(r'^search/$', answer_views.search, name='search-products'),
    url(r'^admin/', admin.site.urls),
    # url(r'^register/', user_views.register, name='register'),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
