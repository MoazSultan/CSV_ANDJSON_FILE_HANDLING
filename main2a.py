import csv

f=open(r'C:\Users\HP\Desktop\module.csv','r')

ro  =  csv.reader(f,  delimiter=',')

lt=list(ro)

print(lt)

for r in lt:

    if len(r)>0:

     print(r[1],r[4])