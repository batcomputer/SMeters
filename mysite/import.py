#Python script running on virtual machine to sort arriving energy readings into their respective tables in SQL database linked with Django app 
import csv,sys,os

project_dir ="/home/batcomputer/mysite/mysite/"

sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django
import datetime
django.setup()

from meters.models import BlockIVModel,SITModel,UdaigiriModel,MainDGModel,GirnarModel
file=open('/home/batcomputer/mysite/chart.csv','r') 
for line in file:       
    line = line.replace(",", " ")
    words =line.split()
    inst=SITModel()
    nump=datetime.datetime.strptime(words[0]+words[1], "%Y-%m-%d%H:%M:%S")
    inst.the_date =nump
    numb = float(words[2])
    inst.the_energy = numb
    inst.save()
     
