from django.db import models


class Products(models.Model):
  maker = models.CharField(max_length=256, blank = True, null=True)
  model = models.IntegerField(max_length=256, primary_key=True)
  type = models.CharField(max_length=256, blank =True, null=True)
  def __unicode__(self):  # Python 3: def __str__(self):
        return "%s - %s - %s" % (self.model, self.maker, self.type)

class PCs(models.Model):
  model = models.ForeignKey(Products, primary_key=True)
  speed = models.IntegerField(max_length=256, blank = True, null=True)
  ram = models.IntegerField(max_length=256, blank = True, null=True)
  hd = models.IntegerField(max_length=256, blank = True, null=True)
  price = models.IntegerField(max_length=256, blank = True, null=True)

  def __unicode__(self):  
        return "%s" % (self.model)

class Laptops(models.Model):
  model = models.ForeignKey(Products, primary_key=True)
  speed = models.IntegerField(max_length=256,blank = True, null=True)
  ram = models.IntegerField(max_length=256, blank = True, null=True)
  hd = models.IntegerField(max_length=256, blank = True, null=True)
  screen = models.IntegerField(max_length=256, blank = True, null=True)
  price = models.IntegerField(max_length=256, blank = True, null=True)
  def __unicode__(self): 
        return "%s" % (self.model)

class Printers(models.Model):
  model = models.ForeignKey(Products, primary_key=True)
  color = models.BooleanField()
  type = models.CharField(max_length=256, blank = True, null=True)
  price = models.IntegerField(max_length=256, blank = True, null=True)
  def __unicode__(self):  # Python 3: def __str__(self):
        return "%s" % (self.model)


