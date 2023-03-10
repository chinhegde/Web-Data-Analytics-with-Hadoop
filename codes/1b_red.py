#!/usr/bin/python3

# REDUCER
import sys

count = dict()

for line in sys.stdin:
    line = line.strip()
    c,v = line.split('\t')


    v = v.split(',')[0]  # REMOVE THIS LINE TO GET (city, country) as key

    if c in count:
        if v not in count[c]:
            count[c].append(v)
    else:
        count[c] = [v]



for k,v in count.items():
   print(k,"-",len(v),"-",", ".join(v),'\n')
