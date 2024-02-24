#!/usr/bin/env python3
# Task1 Mapper: Find the number of tickets raised for the year 2022

import sys  

def mapper(year):
    for line in sys.stdin: 
        columns = line.strip().split(',') 
        if len(columns) == 43: 
            issue_date = columns[4] 
            if str(year) in issue_date: 
                print('%s\t%s' % (year, 1))

mapper(2022)