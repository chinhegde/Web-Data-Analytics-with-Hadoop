#!/usr/bin/python3

# REDUCER
import sys

count = dict()

for line in sys.stdin:
    line = line.strip()
    print(line)
    c,v = line.split(":")

    try:
        v = int(v)
    except ValueError:
        continue

    if c in count:
        if v in count[c]:
            count[c][v] += 1
        else:
            count[c][v] = 1
    else:
        count[c] = {v: 1}

new_data = {k: v for k, v in count.items() if "online" not in k.lower() or "video" not in k.lower()}

for k,v in new_data.items():
    print(k,v)
