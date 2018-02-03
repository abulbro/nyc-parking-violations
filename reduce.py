#!/usr/bin/env python

from __future__ import division
from operator import itemgetter
import sys


current_license = None
current_total = 0
license = None
count = 1
current_val = None

for line in sys.stdin:
    #print line
    line = line.strip().replace(",","").split()
    #print line
    license = line[0] #key
    #try:
    total = float(line[1]) #value1
    #except ValueError:
    #    continue
    #try:
    average = float(line[2]) #value2
        #print average
    #except IndexError:
    #    average = float(line[1])

    if current_license == license:
        current_total += total
        count = count+1
    else:
        average = float(current_total/count)
        if current_license:
            print (str(current_license)+"\t"+ "%.2f" %current_total +","+"%.2f" %average)
            #dummy = 1
        current_total = total
        current_license = license
        average = total
        count = 1


if current_license == license:
    average = float(current_total/count)
    print (str(current_license)+"\t"+ "%.2f" %current_total +","+"%.2f" %average)
