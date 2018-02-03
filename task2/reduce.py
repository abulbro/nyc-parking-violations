#!/usr/bin/env python


from operator import itemgetter
import sys


current_code = None
current_count = 0
code = None

for line in sys.stdin:
    line = line.strip()

    code, count = line.split('\t', 1)

    try:
        count = int(count)
    except ValueError:
        continue

    if current_code == code:
        current_count += count
    else:
        if current_code:
            print '%s\t%s' % (current_code, current_count)
        current_count = count
        current_code = code

if current_code == code:
    print '%s\t%s' % (current_code, current_count)
