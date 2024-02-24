#!/usr/bin/env python3
# Task4 Mapper: What are the top 15 most frequently occurring violation codes?

import sys  

def mapper(year):
    for line in sys.stdin: 
        columns = line.strip().split(',') 
        if len(columns) == 43: 
            issue_date = columns[4] 
            if (str(year) in issue_date):
                violation_code = columns[5]
                print('%s\t%s' % (violation_code, 1))

mapper(2022)