#!/usr/bin/env python3
# Task3 Reducer: What are the number of incidents for which address is missing? Consider the Street Codes attributes, i.e. "Street Code 1" or "Street Code 2" or "Street Code 3". 

import sys

def reducer():
    street_counts = {} 
     
    for line in sys.stdin: 
        line = line.strip()
        street, count = line.strip().split('\t') 

        try:
            count = int(count)
        except ValueError:
            continue 

        street_counts[street] = street_counts.get(street, 0) + count 
        
    sorted_streets = sorted(street_counts.items(), key=lambda x: x[1], reverse=True)
    for street, count in sorted_streets:
        print('%s\t%s' % (street, count)) 

reducer()