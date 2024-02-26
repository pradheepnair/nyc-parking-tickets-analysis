#!/bin/bash
# Run Task1

hdfs dfs -rm -r /big-data/nyc-parking-tickets/task1
#chmod +x map.py reduce.py
hs --mapper $AS1_HOME/task1/mapper.py --reducer $AS1_HOME/task1/reducer.py --input /big-data/nyc-parking-tickets/Parking_Violations_Issued_-_Fiscal_Year_2024_20240220.csv --output /big-data/nyc-parking-tickets/task1