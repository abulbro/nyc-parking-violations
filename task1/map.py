#!/usr/bin/env python

import sys
import string
import csv

for line in sys.stdin:
    row = csv.reader([line], delimiter=',')
    row = list(row)[0]
    if (len(row) == 22):
        value = row[14],row[6],row[2],row[1]
        print(str(row[0]) + '\t' + str(value).replace("(","").replace(")","").replace("'",""))
    else:
        value = row[1], row[5], row[7],row[9]
        print(str(row[0]) + '\t' + str(value).replace("(","").replace(")","").replace("'",""))
