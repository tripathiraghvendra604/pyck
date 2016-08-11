from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Area(models.Model):
    pincode = models.IntegerField()

    def __unicode__(self):
        return self.pincode

class Company(models.Model):
    company = models.CharField(max_length=100)

    def __unicode__(self):
        return self.company

class Delivery(models.Model):
    pincode = models.ForeignKey(Area)
    company = models.ForeignKey(Company)
    price = models.IntegerField()
    prefrence = models.IntegerField()

    class Meta:
        ordering = ['-prefrence']