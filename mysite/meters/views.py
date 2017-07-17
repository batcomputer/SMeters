# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .models import EnergyModel
from django.core import serializers
from django.http import HttpResponse

# Create your views here.
def index(request):
    data= EnergyModel.objects.all()
   
    return render(request,'meters/index.html',{'energykwh': data})

def jason(request):
    objs = EnergyModel.objects.all()
    jsondata = serializers.serialize('json',objs, fields=('energy'))#,'DateandTime'))
    return HttpResponse(jsondata, content_type='application/json')