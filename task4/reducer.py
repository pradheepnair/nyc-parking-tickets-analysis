#!/usr/bin/env python3
# Task4 Reducer: What are the top 15 most frequently occurring violation codes?

import sys

def reducer():
    violation_counts = {} 
     
    for line in sys.stdin: 
        line = line.strip()
        violation_code, count = line.strip().split('\t') 

        try:
            count = int(count)
        except ValueError:
            continue 

        violation_counts[violation_code] = violation_counts.get(violation_code, 0) + count 
        
    sorted_violations = sorted(violation_counts.items(), key=lambda x: x[1], reverse=True)
    for violation_code, count in sorted_violations:
        print('%s\t%s' % (violation_code, count)) 

reducer()