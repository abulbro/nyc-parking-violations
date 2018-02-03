#!/usr/bin/env python

import sys
import string

for row in sys.stdin:

    row = row.strip()

    row = row.split(",")

    key_value = dict()
    if (row[14] == 'T'):
        key_value[str(row[15]) + "," + str(row[17])] = 1
        print(str(key_value).replace("'", "").replace("{","").replace("}","").replace(":","\t"))
    else:
        key_value[str(row[14]) + "," + str(row[16])] = 1
        print(str(key_value).replace("'", "").replace("{","").replace("}","").replace(":","\t"))
