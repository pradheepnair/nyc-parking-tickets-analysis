#!/usr/bin/env python3
# Task2 Reducer: What are the number of states for which tickets have been filed for year 2022? Also provide the list of the states.

import sys

def reducer():
    state_counts = {} 
     
    for line in sys.stdin: 
        line = line.strip()
        state, count = line.strip().split('\t') 

        try:
            count = int(count)
        except ValueError:
            continue 

        state_counts[state] = state_counts.get(state, 0) + count 
        
    sorted_states = sorted(state_counts.items(), key=lambda x: x[1], reverse=True)
    for state, count in sorted_states:
        print('%s\t%s' % (state, count)) 

reducer()