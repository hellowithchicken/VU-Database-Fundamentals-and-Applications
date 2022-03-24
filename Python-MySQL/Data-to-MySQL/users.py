import os, json
import mysql.connector

connection = mysql.connector.connect(host='vudb.notgonnashareongithub.rds.amazonaws.com',
                                     database='Yelp',
                                     user='admin',
                                     password='notgonnashareongithub')
cursor = connection.cursor()

# read JSON file which is in the next parent folder
file = "/Users/IggyMac/OneDrive - UvA/VU work/Example SQL databases/Yelp/archive/yelp_academic_dataset_user.json"
mySql_insert_query = """INSERT INTO Users (user_id, name, fans, joined) 
                        VALUES (%s, %s, %s, %s) """


with open(file, "r") as f:
    data_submit = []
    i = 0
    count = 0
    for line in f:
        data = json.loads(line)
        user_id = data["user_id"]
        name = data["name"]
        fans = data["fans"]
        joined = data["yelping_since"]
        touple = (user_id, name, fans, joined)
        count += 1
        data_submit.append(touple)
        if  count >= 10000:
            cursor.executemany(mySql_insert_query, data_submit)
            connection.commit()
            count = 0
            data_submit = []
        i += 1
        print(i)
    cursor.executemany(mySql_insert_query, data_submit)
    connection.commit()
        