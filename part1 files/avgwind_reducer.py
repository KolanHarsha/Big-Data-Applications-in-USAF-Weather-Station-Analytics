#!/usr/bin/env python

import sys

current_key = None
total_wind_direction = 0
count = 0

for line in sys.stdin:
    
    key, value = line.strip().split('\t')

    # Convert the value to an integer
    try:
        wind_direction = int(value)
    except ValueError:
        continue  # Skip invalid entries

    if current_key != key:
        if current_key is not None:
            average = total_wind_direction / count
            print "%s\t%s" % (current_key, average)

        # Reset variables for the new key
        current_key = key
        total_wind_direction = 0
        count = 0

    total_wind_direction += wind_direction
    count += 1

# Output the last key if needed
if current_key is not None:
    average = total_wind_direction / count
    print "%s\t%s" % (current_key, average)
