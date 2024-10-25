# fileparse.py
#
# Exercise 3.3

import os
import gzip


f=gzip.open('Data/portfolio.csv.gz', 'rt')
headers=next(f).strip().split(',')
print(headers)

sum=0
for line in f:
    row=line.split(',')
    sum=sum+int(row[1])*float(row[2])



print('Total Cost', sum)
f.close()

