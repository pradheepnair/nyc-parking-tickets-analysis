# NYC Parking Ticket Analysis
An exploratory analysis of NYC Parking Tickets for the year 2022 using Hadoop MapReduce

# Business Context 
New York citizens are facing the severe problem of the parking spaces because of the mismatch between the available parking space in the city and the actual number of vehicles present on the city roads. As a result, many of the citizens are issued the parking tickets by City Police department due to the violation of parking rules. As the number of these incidents are increasing at alarming rate, the Police department has decided to analyze the tickets data to find out the frequent patterns present in the parking violations. 

# Business Problem Understanding
The Police department is facing the severe crunch of the internal, trained officer who can help in doing the parking tickets data analysis. For that matter, the department have reached out to your team so that you can help them to identify the patterns out of the huge pile of tickets data with the help of the latest tools / technologies available in the data analytics field. Your team have been appointed to take a closer look at the records of parking tickets of the New York City for the year 2022 to 

[x] Identify the factors causing the parking tickets  
[x] Recommend the ways that can help to improve upon the better management of the parking space

# Data Understanding 
For this analysis, the department is expecting your team to explore the usage of HDFS and Hadoop Map Reduce for the storage and querying the parking tickets data respectively. The data is available at the city portal NYC parking tickets for year 2022.  The data dictionary can also be read from the same source. 

Parking Violations Issuance datasets contain violations issued during the respective fiscal year. The Issuance datasets are not updated to reflect violation status, the information only represents the violation(s) at the time they are issued. Since appearing on an issuance dataset, a violation may have been paid, dismissed via a hearing, statutorily expired, or had other changes to its status.  

# Data preparation and Exploratory Data Analysis
You are supposed to make utilizations of all the appropriate data pre-processing techniques on the given data set. If required, make appropriate assumptions and make it explicitly known while using them in the query. Make appropriate selection of the attributes with sound justification for the same. The data set allows for several new combinations of attributes and attribute exclusions, or the modification of the attribute type (categorical, integer, or real) depending on the purpose of the analysis.

# Expected Outcomes 
You are expected to find out the answers to following questions. 

1) Find the number of tickets raised for the year 2022.
2) What are the number of states for which tickets have been filed for year 2022? Also provide the list of the states. 
3) What are the number of incidents for which address is missing? Consider the Street Codes attributes, i.e. "Street Code 1" or "Street Code 2" or "Street Code 3". 
4) What are the top 15 most frequently occurring violation codes?
5) What is the observation with respect to the parking tickets issued based on the vehicle make?

# The results should consists of 

[x] A document file containing Python code for Mapper and Reducer to the above Five questions that you have written to extract the answers and Screen shots of the output for the same
[x] Individual student need to complete and submit their report seperately
[x] Name the document file in format like "bitsid.doc" only. Don't add anything into the file names. 
[x] Make sure that you upload the file well ahead of deadline.
[x] Note - This is a group assignment, Submission is expected per group

# References
[NYC parking tickets for year 2022](https://data.cityofnewyork.us/City-Government/Parking-Violations-Issued-Fiscal-Year-2020/pvqr-7yc4)