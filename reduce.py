#!/usr/bin/env python

import sys
import string
import operator

currentkey = None
weekendlist = [5, 6, 12, 13, 19, 20, 26, 27]
weeksum = 0
weekendsum = 0
for line in sys.stdin:
    line = line.strip()
    key, values = line.split('\t',1)
    key = key.strip()
    values = values.strip().split("-")
    date = int(values[2])
    if key==currentkey:
        if date in weekendlist:
            weekendsum += 1
        else:
            weeksum += 1
    else:
        if currentkey:
            average_weekend = float(weekendsum/8.00)
            average_week = float(weeksum/23.00)
            print(str(currentkey) + "\t" + "%.2f" %average_weekend + "," + "%.2f" %average_week)

        currentkey = key
        weeksum = 0
        weekendsum = 0
        if date in weekendlist:
            weekendsum += 1
        else:
            weeksum += 1

average_weekend = float(weekendsum/8.00)
average_week = float(weeksum/23.00)
print(str(currentkey) + "\t" + "%.2f" %average_weekend + "," + "%.2f" %average_week)
