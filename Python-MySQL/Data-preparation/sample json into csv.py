#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 07:46:05 2021

@author: IggyMac
"""
                
import csv
import json
import random

working_directory = "/Users/IggyMac/OneDrive - UvA/VU work/Example SQL databases/Yelp/archive/"
infile = open(working_directory + "yelp_academic_dataset_review.json","r")

row_n = 0
for row in infile:
    row_n += 1
    if row_n == 1:
       data = json.loads(row) 
       
sample_rows = random.sample(range(row_n), 1500000)
sample_rows.sort()

outfile = open(working_directory + "csv/review_sample.csv","w+")
writer = csv.DictWriter(outfile, fieldnames = list(data.keys()))
writer.writeheader()

counter = -1
print(counter)
infile = open(working_directory + "yelp_academic_dataset_review.json","r")
for row in infile:
    counter += 1
    if counter in sample_rows:
        sample_rows.remove(counter)
        data = json.loads(row)
        writer.writerow(data)
    else:
        continue
    print(counter)
    
    
        

                