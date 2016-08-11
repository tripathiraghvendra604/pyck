from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Info(models.Model):
    pincode = models.IntegerField()

    delhivery = models.CharField(max_length=5)
    delhivery_limit = models.IntegerField()

    fedex = models.CharField(max_length=5)
    fedex_limit = models.IntegerField()

    dotzot = models.CharField(max_length=5)
    dotzot_limit = models.IntegerField()

    dtdc = models.CharField(max_length=5)

    indiapost = models.CharField(max_length=5)

    pref1 = models.CharField(max_length=100)
    pref2 = models.CharField(max_length=100)
    pref3 = models.CharField(max_length=100)
    pref4 = models.CharField(max_length=100)
    pref5 = models.CharField(max_length=100)

    def __unicode__(self):
        return self.pincode
