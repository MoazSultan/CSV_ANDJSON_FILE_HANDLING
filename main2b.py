import csv

f1 = open(r'C:\Users\HP\Desktop\module.CSV','r')
f2 = open(r'C:\Users\HP\Desktop\module2.CSV','w')

ro = csv.reader( f1,   delimiter=',')
wo = csv.writer( f2,   delimiter=',')

lt=list(ro)



for r in lt:

    if len(r) >  0:

        new_row=(r[0:4] + [float(r[4]) + 5])
        print(new_row)
        wo.writerow(new_row)

f1.close()
f2.close()




