#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 17:11:04 2021

@author: IggyMac
"""

from sqlalchemy import create_engine
from sqlalchemy.types import String, Integer, DateTime
import pandas as pd
import os
import json

engine = create_engine('mysql+mysqlconnector://admin:pRotection101.4@vudb.cp9k56qqj8ei.eu-central-1.rds.amazonaws.com/Yelp')

# read JSON file and calculate number of lines
working_directory = "/Users/IggyMac/OneDrive - UvA/VU work/Example SQL databases/Yelp/archive"
file_name = "/yelp_academic_dataset_checkin.json"
save_location = "/csv/checkins"
file = working_directory + file_name
num_lines = sum(1 for line in open(file))


final_csv = pd.DataFrame()
file_no = 0 

with open(file, "r") as f:
    count = 0
    for line in f:
        data = json.loads(line)
        
        business_id = data["business_id"]
        date = data["date"]
        date = date.split(", ")
        dict_df = {"business_id": business_id,
                   "date": date}
        df = pd.DataFrame(dict_df)
        df.head()
        print(count/num_lines*100)
        count += 1
        final_csv = final_csv.append(df)
        # once number of rows in file are above 1 million, write the file
        if len(final_csv) > 1000000:
            final_csv.to_csv(working_directory + save_location + f"/check_ins_{file_no}.csv", index = False)
            file_no += 1
            final_csv = pd.DataFrame()
        
        
#exit() 
#df.to_sql('CheckIns', 
#        engine, 
#        if_exists='append', 
#        index=False, 
#        dtype={"business_id": String(),
#               "date": DateTime()})
        
        
        