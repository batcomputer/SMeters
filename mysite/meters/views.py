# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .models import SITModel, BlockIVModel,UdaigiriModel
from django.core import serializers
from django.http import HttpResponse

# Create your views here.
def index(request):
    data= SITModel.objects.all()
    
    return render(request,'meters/index.html',{'energykwh': data})

def jason(request):
    objs = SITModel.objects.all()
    jsondata = serializers.serialize('json',objs, fields=('the_energy','the_date'))
    return HttpResponse(jsondata, content_type='application/json')


def hostel(request):
    objs = BlockIVModel.objects.all()
    jsondata = serializers.serialize('json',objs, fields=('the_energydata','the_time'))
    return HttpResponse(jsondata, content_type='application/json')
