#!/usr/bin/env python3
# Task5 Reducer: What is the observation with respect to the parking tickets issued based on the vehicle make?

import sys

def reducer():
    vehicle_counts = {} 
     
    for line in sys.stdin: 
        line = line.strip()
        vehicle_make, count = line.strip().split('\t') 

        try:
            count = int(count)
        except ValueError:
            continue 

        vehicle_counts[vehicle_make] = vehicle_counts.get(vehicle_make, 0) + count 
        
    sorted_vehicles = sorted(vehicle_counts.items(), key=lambda x: x[1], reverse=True)
    for vehicle_make, count in sorted_vehicles:
        print('%s\t%s' % (vehicle_make, count)) 

reducer()