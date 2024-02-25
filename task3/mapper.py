#!/usr/bin/env python3
# Task3 Mapper: What are the number of incidents for which address is missing? Consider the Street Codes attributes, i.e. "Street Code 1" or "Street Code 2" or "Street Code 3". 

import sys  

def mapper(year):
    for line in sys.stdin: 
        columns = line.strip().split(',') 
        if len(columns) == 43: 
            issue_date = columns[4] 
            if (str(year) in issue_date):
                street_code1 = int(columns[9])
                street_code2 = int(columns[10])
                street_code3 = int(columns[11])
                if (street_code1 == 0):
                    print('%s\t%s' % ('Street Code 1', 1)) 
                if (street_code2 == 0):
                    print('%s\t%s' % ('Street Code 2', 1)) 
                if (street_code3 == 0):
                    print('%s\t%s' % ('Street Code 3', 1)) 
                if (street_code1 == 0 and street_code2 == 0):
                    print('%s\t%s' % ('Street Code 1 & 2', 1)) 
                if (street_code1 == 0 and street_code3 == 0):
                    print('%s\t%s' % ('Street Code 1 & 3', 1)) 
                if (street_code2 == 0 and street_code3 == 0):
                    print('%s\t%s' % ('Street Code 2 & 3', 1)) 
                if (street_code1 == 0 and street_code2 == 0 and street_code3 == 0):
                    print('%s\t%s' % ('Street Code 1, 2 & 3', 1))  

mapper(2022)