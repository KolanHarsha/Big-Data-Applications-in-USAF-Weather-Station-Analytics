#!/usr/bin/env python

import sys

for line in sys.stdin:
    Id = line[4:10]
    distance = line[78:84].strip()
    q = line[84]

    if distance != '999999' and q in '01459':
        # Output key-value pairs: (Id, distance)
        print "%s\t%s" % (Id, distance)
