#!/usr/bin/python3
import sys

# NOTE: City also considers University names listed with city, country

for x,line in enumerate(sys.stdin):
    if x == 0: continue
    line = line.strip()
    line = line.split('\t')
    print(line[3]+'\t 1')


