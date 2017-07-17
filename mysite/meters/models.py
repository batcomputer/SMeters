# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class EnergyModel(models.Model):
    DateandTime = models.DateTimeField(auto_now=False, auto_now_add=False)

    energy =models.FloatField(max_length=20)

    def __str__(self):

        return str(self.energy)
        