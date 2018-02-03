#!/usr/bin/env python

import sys
import string
import csv

for line in sys.stdin:
    row = csv.reader([line], delimiter=',')
    row = list(row)[0]
    key_value = dict()
    key_value[row[16]] = 1
    print(str(key_value).replace("'", "").replace('{','').replace('}','').replace(':','\t'))
