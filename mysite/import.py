import csv,sys,os

project_dir ="/home/batcomputer/mysite/mysite/"

sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django
import datetime
django.setup()

from meters.models import EnergyModel

file=open('/home/batcomputer/mysite/chart.csv','r') 
for line in file:       
        line = line.replace(",", " ")
        words =line.split()
        inst=EnergyModel()
        #inst.date= words[0]
        #num = date(words[0])
        #nump=datetime.datetime.strptime(words[0]+words[1], "\"%Y-%m-%d%H:%M\"")
      
        nump=datetime.datetime.strptime(words[0]+words[1], "\"%Y-%m-%d%H:%M\"")
        inst.DateandTime =nump

 
        #nume= datetime.datetime.strptime(words[1], "%H:%M\"")
      
        #inst.time= words[1]

        #inst.energy = words[2]
        numb = float(words[2])
        inst.energy = numb
        inst.save()
