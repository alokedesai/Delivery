from django.contrib import admin
from products.models import Products,PCs,Laptops,Printers
# Register your models here.


admin.site.register(Products)
admin.site.register(PCs)
admin.site.register(Laptops)
admin.site.register(Printers)