#!/usr/bin/env python

import sys
import string

currentkey = None
count = 0
prev_val = None

for line in sys.stdin:
    line = line.strip()
    key, value = line.split('\t',1)
    if key == currentkey:
        count = count + 1
    else:
        if currentkey:
            if count == 1:
                print(str(currentkey) + '\t' + str(prev_val))

        currentkey = key
        count = 1
        prev_val = value

if count == 1:
    print(str(key) + '\t' + str(value))
