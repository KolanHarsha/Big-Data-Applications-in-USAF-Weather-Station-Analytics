#!/usr/bin/env python

import sys

current_key = None

for line in sys.stdin:
    # Split the input into key and value
    key, value = line.strip().split('\t')

    if current_key == key:
        # Print the key-value pair
        print "%s\t%s" % (key, value)
    else:
        # Update the current key
        current_key = key

        # Print the key-value pair
        print "%s\t%s" % (key, value)    