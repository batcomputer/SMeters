import csv
file=open('chart.csv','r') 
for line in file:
        line = line.replace(",", " ")
        words =line.split()
        dab=Dab()
        dab.date= words[0]
        dab.time= words[1]
        dab.energy = words[2]
file.close() 

