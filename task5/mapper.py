#!/usr/bin/env python3
# Task5 Mapper: What is the observation with respect to the parking tickets issued based on the vehicle make?

import sys  

def mapper(year):
    for line in sys.stdin: 
        columns = line.strip().split(',') 
        if len(columns) == 43: 
            issue_date = columns[4] 
            if (str(year) in issue_date):
                vehicle_make = columns[7]
                if len(vehicle_make.strip()) > 0:
                    print('%s\t%s' % (vehicle_make, 1))
                else:
                    print('%s\t%s' % ('-', 1))

mapper(2022)