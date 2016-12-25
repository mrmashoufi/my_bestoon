from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class kharj(models.Model):
    Onvan = models.CharField(max_length = 255)
    Zaman = models.DateTimeField()
    Meghdar = models.BigIntegerField()
    Karbar = models.ForeignKey(User)
    def __unicode__(self):
        return "{} - Mablagh : (- {} ) - Dar Tarikh :{}".format(self.Onvan,self.Meghdar,self.Zaman)

class daramad(models.Model):
    Onvan = models.CharField(max_length = 255)
    Zaman = models.DateTimeField()
    Meghdar = models.BigIntegerField()
    Karbar = models.ForeignKey(User)
    def __unicode__(self):
        return "{} - Mablagh :( +{} ) - Dar Tarikh :{}".format(self.Onvan,self.Meghdar,self.Zaman)
