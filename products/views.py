from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse


# Create your views here.
from products.models import Product
from cart import Cart

def add_to_cart(request,product_id, quantity):
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.add(product, product.price, quantity)


def remove_from_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.remove(product)
def update(request,product_id, quantity):
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.update(product, quantity, product.price)

def get_cart(request):
    cart = Cart(request)
    total = cart.summary()
    return render(request,'products/cart.html', dict(cart=Cart(request), total=total*100))
def index(request):
    products = Product.objects.all()[:5]
    cart = Cart(request)
    amount = cart.count()
    return render(request, "products/index.html", dict(products = products, amount=amount))
    
def add(request,prod,amount):
    add_to_cart(request, prod, amount)
    
    return HttpResponse(prod + "- " + amount)
