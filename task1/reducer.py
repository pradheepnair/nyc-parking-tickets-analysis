#!/usr/bin/env python3
# Task1 Reducer: Find the number of tickets raised for the year 2022

import sys

def reducer():
    current_year = None
    ticket_count = 0
     
    for line in sys.stdin: 
        year, count = line.strip().split('\t') 
        try:
            count = int(count)
        except ValueError:
            continue 

        if current_year != year:
            if current_year is not None:
                print('%s\t%s' % (current_year, ticket_count))
            current_year = year
            ticket_count = 0 

        ticket_count += count 

    if current_year is not None:
        print('%s\t%s' % (current_year, ticket_count))

reducer()