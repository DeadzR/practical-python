# pcost.py
#
# Exercise 1.27
import csv
import sys
def portfolio_cost(filename):


    f=open(filename, 'rt')
    rows=csv.reader(f)
    headers=next(rows)
    print(headers)


    sum=0
    for line in rows:
       
        try:
            sum=sum+int(line[1])*float(line[2])
        except ValueError:
            print("cannot add value")



    print('Total Cost', sum)
    f.close()


if len(sys.argv)==2:
    filename=sys.argv[1]
else:
    filename='Data/missing.csv'

print(filename)
portfolio_cost(filename)