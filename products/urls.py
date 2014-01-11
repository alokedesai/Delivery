from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ecommerce.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

   url(r'^$', 'products.views.index', name='index'),
   url(r'^cart/', 'products.views.get_cart', name="cart"),
   url(r'^(?P<prod>\d+)/(?P<amount>\d+)$', "products.views.add", name='add'),
)