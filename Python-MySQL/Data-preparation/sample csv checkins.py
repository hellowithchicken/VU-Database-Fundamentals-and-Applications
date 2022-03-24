import pandas as pd
import os

# define fraction of data we want

fraction = 0.187

working_directory = "/Users/IggyMac/OneDrive - UvA/VU work/Example SQL databases/Yelp/archive/csv/checkins/"
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
    
final_file.to_csv(working_directory + "sampled_checkins.csv")