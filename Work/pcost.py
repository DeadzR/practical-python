# pcost.py
#
# Exercise 1.27
f=open('Data/portfolio.csv', 'rt')
headers=next(f).strip().split(',')
print(headers)

sum=0
for line in f:
    row=line.split(',')
    sum=sum+int(row[1])*float(row[2])



print('Total Cost', sum)
f.close()