#!/usr/bin/env python

import sys
import string

ny = 0
other = 0

for line in sys.stdin:

    line = line.strip()

    key, value = line.split('\t',1)

    if key == 'NY':
        ny += 1
    else:
        other += 1

print('NY' + '\t' + str(ny))
print('Other' + '\t' + str(other))
