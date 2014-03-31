from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  	url(r'^add/', 'products.views.add', name="add"),
  	url(r'^$', 'products.views.index', name="index"),
    url(r'^price/', 'products.views.price', name="price"),
    url(r'^minspecs/', 'products.views.minSpecs', name="minSpecs"),
    url(r'^maker', 'products.views.maker', name="maker"),
    url(r'^budget/', 'products.views.budget', name="budget"),
)