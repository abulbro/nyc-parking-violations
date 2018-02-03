#!/usr/bin/env python

import sys
import string

import csv

#parking_v = csv.reader(open("/Users/syedalishehryar/OneDrive/Big Data/project1/parking-violations.csv"))
for line in sys.stdin:
    line = line.strip()
#for row in parking_v:
    #print(str(line) + "\n")
    row = line.split(',')
    #print(row)
    key = row[2]
    value = 1
    myDict2 = {key:value}
    sys.stdout.write(str(myDict2).replace("{","").replace("}","").replace(":","\t").replace("(","").replace(")","").replace("'","") + "\n")
