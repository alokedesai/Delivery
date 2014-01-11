from django.db import models
from django.contrib.auth.models import User, UserManager

# Create your models here.

class Type(models.Model):
  name = models.CharField(max_length=300)

  def __unicode__(self):
    return self.name
class Product(models.Model):
  name = models.CharField(max_length=300)
  description = models.TextField()
  price = models.DecimalField(max_digits=6,decimal_places=2)
  type = models.ForeignKey(Type)
  def __unicode__(self):  # Python 3: def __str__(self):
        return "%s - %s" % (self.name, self.description)
