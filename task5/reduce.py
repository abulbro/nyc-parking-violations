#!/usr/bin/env python

import sys
import string

currentkey = None
count = 0
violations = ['key', count]

for line in sys.stdin:
    line = line.strip()
    key, values = line.split('\t',1)

    key = key.strip()
    if key==currentkey:
        count += 1
    else:
        if currentkey:
            if count > violations[1]:

                violations[0] = currentkey
                violations[1] = count

        currentkey = key
        count = 1

if count > violations[1]:

    violations[0] = currentkey
    violations[1] = count

print(str(violations[0])+"\t"+str(violations[1]))
