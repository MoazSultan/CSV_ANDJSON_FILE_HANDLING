import csv

f = open(r'C:\Users\HP\Desktop\module.csv','r')

wo = csv.writer(f, delimiter =',')

num= int(input("enter the number of students"))

list=[]

for i in range(num):
    rn=input("enter the student roll number")
    n=input("enter the student name")
    a=int(input("enter the student age"))
    c=int(input("enter the student Class"))
    p=float(input("enter the student percentage"))
    list.append([rn,n,a,c,p])

wo.writerows(list)
f.close()