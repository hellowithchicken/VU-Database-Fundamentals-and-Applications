#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 17:11:04 2021

@author: IggyMac
"""

import json
import mysql.connector

connection = mysql.connector.connect(host='vudb.cp9k56qqj8ei.eu-central-1.rds.amazonaws.com',
                                     database='Yelp',
                                     user='admin',
                                     password='pRotection101.4')
cursor = connection.cursor()

# read JSON file which is in the next parent folder
file = "/Users/IggyMac/OneDrive - UvA/VU work/Example SQL databases/Yelp/archive/yelp_academic_dataset_review.json"
mySql_insert_query = """INSERT INTO Reviews (Id, BusinessId, UserId, Stars, Cool, Funny, Useful, Date) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s) """

num_lines = sum(1 for line in open(file))

chunk_size = 100

with open(file, "r") as f:
    data_submit = []
    i = 0
    count = 0
    for line in f:
        data = json.loads(line)
        
        review_id = data["review_id"]
        user_id = data["user_id"]
        business_id = data["business_id"]
        stars = data["stars"]
        funny = data["funny"]
        date = data["date"]
        useful = data["useful"]
        cool = data["cool"]

        touple = (review_id, business_id, user_id,
                  stars, cool, funny,
                  useful, date)
        count += 1
        data_submit.append(touple)
        if  count >= chunk_size:
            cursor.executemany(mySql_insert_query, data_submit)
            connection.commit()
            i += 1
            print(i/(num_lines/chunk_size) * 100)
            count = 0
            data_submit = []
    cursor.executemany(mySql_insert_query, data_submit)
    connection.commit()
        