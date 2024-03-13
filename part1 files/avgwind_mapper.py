#!/usr/bin/env python

import sys

for line in sys.stdin:
    
    year_month = line[15:21]
    wind_direction = line[60:63]
    q = line[63]
    if wind_direction != '999' and q in '01459':
        # Output key-value pairs: (year_month, wind_direction)
        print "%s\t%s" % (year_month, wind_direction)
