#!/usr/bin/env python

import sys
import string

for line in sys.stdin:
    line = line.strip().replace("\"","")
#for row in parking_v:
    #print(str(line) + "\n")
    row = line.split(',')
    #print(row)
    key = row[2] #plate_type
    #print key

    if len(key)>3 or len(key)<3:
        continue
    if row[12]:
        value = float(row[12]),1.00 #total_amt,avg
    else:
        value = 0.00,1.00
    myDict = {key:value}
    sys.stdout.write(str(myDict).replace("{","").replace("}","").replace(":","\t").replace("(","").replace(")","").replace("'","")+"\n")
