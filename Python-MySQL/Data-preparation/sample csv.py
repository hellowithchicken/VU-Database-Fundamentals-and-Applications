import pandas as pd
import os


# get info about the json file, number of rows
working_directory = "/Users/IggyMac/OneDrive - UvA/VU work/Example SQL databases/Yelp/archive/"
infile = open(working_directory + "yelp_academic_dataset_review.json","r")

row_n = 0
for row in infile:
    row_n += 1
    
# define fraction of data we want

rows_wanted = 1500000
fraction = rows_wanted/row_n

exit()

working_directory = "/Users/IggyMac/OneDrive - UvA/VU work/Example SQL databases/Yelp/archive/csv/"
list_files = os.listdir(working_directory)

final_file = pd.DataFrame()
for file in list_files:
    if ".csv" not in file:
        # skip non-csv files
        continue
    # read data
    print(file)
    data = pd.read_csv(working_directory+file)
    sampled_data = data.sample(frac = fraction)
    final_file = final_file.append(sampled_data)