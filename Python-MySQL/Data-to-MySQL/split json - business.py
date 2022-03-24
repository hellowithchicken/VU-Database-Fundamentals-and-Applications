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
infile = open(working_directory + "yelp_academic_dataset_business.json","r")

row_n = 0
for row in infile:
    row_n += 1
    
chunk_size = 50000


infile = open(working_directory + "yelp_academic_dataset_business.json","r")
counter = 0
file_number = 0
for row in infile:
    data = json.loads(row)
    if counter == 0:
        file_number += 1
        outfile = open (working_directory + "csv/business/business_split_" + str(file_number) + ".csv","w+")
        writer = csv.DictWriter(outfile, fieldnames = list(data.keys()))
        writer.writeheader()
    writer.writerow(data)
    counter += 1
    print(counter)
    if counter > chunk_size:
        counter = 0
        
        

                