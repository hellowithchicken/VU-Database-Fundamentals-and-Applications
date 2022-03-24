#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 09:33:16 2021

@author: IggyMac
"""

from sqlalchemy import create_engine
from sqlalchemy.types import String, Integer, DateTime
import pandas as pd
import os

engine = create_engine('mysql+mysqlconnector://admin:pRotection101.4@vudb.cp9k56qqj8ei.eu-central-1.rds.amazonaws.com/Yelp')


working_directory = "/Users/IggyMac/OneDrive - UvA/VU work/Example SQL databases/Yelp/archive/csv/sampled-to-upload/"
list_files = os.listdir(working_directory)

for file in list_files:
    if ".csv" not in file:
        # skip non-csv files
        continue
    # read data
    data = pd.read_csv(working_directory+file)
    # drop text file
    data = data.drop(columns=['Unnamed: 0'])
    data.sort_values(by = ["date"], inplace = True)
    # create list for diving the file into chunks
    lent = range(0, len(data), 10000)
    print(file)
    for i in range(len(lent)-1):
        data_to_upload = data[lent[i]:lent[i+1]]
        data_to_upload.to_sql('CheckIns', 
                                engine, 
                                if_exists='append', 
                                index=False, 
                                dtype={"business_id": String(),
                                       "date": DateTime()})
        print(i)
        
        