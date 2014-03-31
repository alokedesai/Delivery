import random
import sys, os
os.environ['DJANGO_SETTINGS_MODULE'] = 'ecommerce.settings'
from django.conf import settings
from products.models import Products,PCs, Laptops, Printers
makers = ["Apple", "HP", "Lenovo", "Dell", "Sony"]
printerType=["laser", "ink-jet"]
colorVal = [True,False]
# add 100 pcs
for i in range(1,100):
	product = Products(maker=makers[random.randint(0,4)], model=i, type="PC")
	product.save()
	ram = random.uniform(1, 16)
	speed = random.uniform(1,4)
	hd = random.randint(100,1000)
	price = random.uniform(500,2000)
	ram = float(format(ram, ".2f"))
	speed = float(format(speed, ".2f"))
	price = float(format(price, ".2f"))

	pc = PCs(model=product, ram=ram,speed=speed, hd=hd, price=price)
	pc.save()
# add 100 laptops
for i in range(100,200):
	product = Products(maker=makers[random.randint(0,4)], model=i, type="Laptop")
	product.save()
	ram = random.uniform(1, 16)
	speed = random.uniform(1,4)
	hd = random.randint(100,1000)
	price = random.uniform(500,2000)
	screen = random.uniform(10,22)
	ram = float(format(ram, ".2f"))
	speed = float(format(speed, ".2f"))
	price = float(format(price, ".2f"))
	screen = float(format(screen, ".2f"))
	laptop = Laptops(model = product, speed= speed, ram=ram, hd=hd, price=price, screen=screen)
	laptop.save()

# add 100 printers
for i in range(200,300):
	product = Products(maker=makers[random.randint(0,4)], model=i, type="Printer")
	product.save()
	color= colorVal[random.randint(0,1)]
	type = printerType[random.randint(0,1)]
	price = random.uniform(50, 1000)
	price = float(format(price, ".2f"))

	printer = Printers(model=product, type=type,color=color,price=price)
	printer.save()

