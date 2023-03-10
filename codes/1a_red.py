#!/usr/bin/python3

# REDUCER
import sys

count = dict()

for line in sys.stdin:
    line = line.strip()
    c,v = line.split('\t')


    c = c.split(',')[0]  # REMOVE THIS LINE TO GET (city, country) as key
    try:
        v = int(v)
    except ValueError:
        continue

    if c in count:
        count[c] += int(v)
    else:
        count[c] = int(v)

# TO PRINT ALL CITIES AND TOTAL COUNT

#for k,v in count.items():
#   print(k,v)

top10 = dict(sorted(count.items(), key=lambda item: item[1], reverse  = True)[:10])

for k,v in top10.items():
    print(k,v)
