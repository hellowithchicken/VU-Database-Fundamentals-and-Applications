#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 09:33:16 2021

@author: IggyMac
"""

from sqlalchemy import create_engine
from sqlalchemy.types import String, Integer, DateTime, JSON, FLOAT
import pandas as pd
import os

engine = create_engine('mysql+mysqlconnector://admin:notgonnashareongithub@vudb.notgonnashareongithub.rds.amazonaws.com/Yelp')


working_directory = "/Users/IggyMac/OneDrive - UvA/VU work/Example SQL databases/Yelp/archive/csv/business-to-upload/"
list_files = os.listdir(working_directory)

for file in list_files:
    if ".csv" not in file:
        # skip non-csv files
        continue
    # read data
    print(file)
    data = pd.read_csv(working_directory+file)
    # drop text file
    data = data.drop(columns=['stars', "review_count", "hours"])
    # create list for diving the file into chunks
    data.to_sql('Businesses', 
                            engine, 
                            if_exists='append', 
                            index=False, 
                            dtype={"business_id": String(),
                                   "name": String(),
                                   "address": String(),
                                   "city": String(),
                                   "state": String(),
                                   "postal_code": String(),
                                   "latitude": FLOAT(),
                                   "longitude": FLOAT(),
                                   "is_open":  Integer(),
                                   "attributes": JSON(),
                                   "categories": String()
                                   })
        
        