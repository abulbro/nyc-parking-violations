#!/usr/bin/env python

import sys
import string

for row in sys.stdin:
    row = row.split(',')
    mapper_dictionary = dict()
    mapper_dictionary[row[2]] = row[1]
    print(str(mapper_dictionary).replace("'", "").replace('{','').replace('}','').replace(':','\t'))
