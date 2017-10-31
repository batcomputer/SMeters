# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class SITModel(models.Model):

    the_date= models.DateTimeField(auto_now=False, auto_now_add=False)
    the_energy = models.FloatField(max_length=20)

    def __str__(self):

        return str(self.the_energy)
  

class BlockIVModel(models.Model):

    the_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    the_energydata = models.FloatField(max_length=20)

    
    def __str__(self):

        return str(self.the_energydata)        

class MainDGModel(models.Model):
    the_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    the_energydata = models.FloatField(max_length=20)

    def __str__(self):

        return str(self.the_energydata)

class UdaigiriModel(models.Model):
    the_time= models.DateTimeField(auto_now=False, auto_now_add=False)
    the_energydata = models.FloatField(max_length=20)        


    def __str__(self):

        return str(self.the_energydata)


class GirnarModel(models.Model):
    the_time= models.DateTimeField(auto_now=False, auto_now_add=False)
    the_energydata = models.FloatField(max_length=20)        


    def __str__(self):

        return str(self.the_energydata)       
