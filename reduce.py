#!/usr/bin/env python

import sys
import string

currentkey = None
count = 0
max_violations = dict()

for line in sys.stdin:

    line = line.strip()

    key, value = line.split('\t',1)
    if key==currentkey:
        count += 1
    else:

        if currentkey:
            max_violations[currentkey] = count
        currentkey = key
        count = 1
max_violations[currentkey] = count
final_dict=dict(sorted(max_violations.items(), key=lambda x: x[1],reverse=True)[:20])
for k,v in final_dict.iteritems():
    k = k.split(",")
    print(str(k).replace("'","").replace("[","").replace("]","") + "\t" + str(v))
