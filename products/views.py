from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.db.models import Min
from products.models import Products,PCs, Laptops, Printers

def convertInt(string):
    try:
        return int(string)
    except ValueError:
        if string == '':
            return None
        return string 
def index(request):
    return render(request, "products/index.html")
def add(request):
    error = False
    added = False
    if request.method =="POST":
        manufacturer = request.POST.get("maker")

        # will return empty string if the field is empty
        model = (request.POST.get("model"))
        speed = convertInt(request.POST.get("speed"))
        RAM = convertInt(request.POST.get("ram"))
        hd = convertInt(request.POST.get("hd"))
        price = convertInt(request.POST.get("price"))
      
        if not model or not speed or not maker or not RAM or not hd or not price:
            error = True
        # check if the user entered a model number and that no PC exists with that model number
        else:
            try:
                Products.objects.get(model=model)
            except ObjectDoesNotExist:
                prod = Products(maker=manufacturer, model=model, type="PC")
                prod.save()
                pc = PCs(model= prod, speed=speed, ram=RAM, hd=hd, price=price)        
                pc.save()
                added= True
    return render(request, "products/add.html", dict(added= added, error = error))

def price(request):
    price = (request.GET.get("price"))
    closest = None
    if price:
        price = int(price)
        computers = PCs.objects.all()
        closestPrice = abs(computers[0].price - price)
        closest = computers[0]
        for computer in computers:
            print "closest.price is " + str(closest.price)
            print "comparing " + str(abs(computer.price - price)) + " to " + str(closest.price)
            print " "
            if abs(computer.price - price) < closestPrice:
                closest = computer
                closestPrice = computer.price - price
    return render(request, "products/price.html", dict(closest = closest))

def minSpecs(request):
    speed = (request.GET.get("speed"))
    ram = (request.GET.get("ram"))
    hd = (request.GET.get("hd"))
    screen = (request.GET.get("screen"))
    results = []
    error = False
    if 'speed' in request.GET:
        if not speed or not ram or not hd or not screen:
            error = True
        else:
            speed = int(speed)
            ram = int(ram)
            screen = int(screen)
            hd = int(hd)
            results = Laptops.objects.filter(speed__gte= speed, ram__gte= ram, hd__gte= hd, screen__gte= screen)
        
    return render(request, "products/minspecs.html", dict(results = results, error=error))
    # get the cheapest
def maker(request):
    maker = request.GET.get("maker")

    pc = []
    laptop = []
    printer = []
    if maker:
        # get all the PCs
        pc = PCs.objects.filter(model__maker=maker)
        laptop = Laptops.objects.filter(model__maker=maker)
        printer = Printers.objects.filter(model__maker=maker)
    return render(request, "products/makers.html", dict(pc = pc, laptop=laptop, printer=printer))
# this question was phrased in a weird way. Since we're finding the cheapeast result, the budget isn't
#that constrianing  
def budget(request):
    params = True
    price = request.GET.get("price")
    speed = request.GET.get("speed")

    error = False
    cheapestPC = None
    cheapestPrinter = None
    if not price or not speed:
        if "price" in request.GET:
            error = True
        else:     
        #don't show the no combinatoin error 
            params = False
    else:
        price = int(price)
        speed = int(speed)

        # get pc and printer min prices
        pc_min = PCs.objects.filter(speed__gte=speed).aggregate(Min("price"))
        printer_min = Printers.objects.all().aggregate(Min("price"))

        print pc_min

                   
        pc = PCs.objects.filter(price=pc_min["price__min"], speed__gte=speed)
        if pc_min["price__min"] and pc_min["price__min"] + printer_min["price__min"] <= price:
           
            # get the printer
            printer = Printers.objects.filter(price = printer_min["price__min"])

            # check if there's a color printer in this combination 
            color =  printer.filter(color=True)
            cheapestPC = pc[0]
            if color:
                cheapestPrinter = color[0]
            else:
                cheapestPrinter = printer[0]

    return render(request, "products/budget.html", dict(printer = cheapestPrinter, pc = cheapestPC, error=error, params=params))


    
    
