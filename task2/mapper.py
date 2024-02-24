#!/usr/bin/env python3
# Task2 Mapper: What are the number of states for which tickets have been filed for year 2022? Also provide the list of the states.

import sys  

def mapper(year):
    for line in sys.stdin: 
        columns = line.strip().split(',') 
        if len(columns) == 43: 
            issue_date = columns[4] 
            if str(year) in issue_date: 
                state = columns[2] 
                print('%s\t%s' % (state, 1))

mapper(2022)