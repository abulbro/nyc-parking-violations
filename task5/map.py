#!/usr/bin/env python

import sys
import string

for row in sys.stdin:
    row = row.strip()
    row = row.split(",")
    map_dict = dict()
    map_dict[str(row[14]) + ","+ str(row[16])] = 1
    print(str(map_dict).replace("'", "").replace("{","").replace("}","").replace(":","\t"))
