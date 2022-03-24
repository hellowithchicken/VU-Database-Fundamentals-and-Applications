import os
import pandas as pd
import numpy as np

data = pd.read_csv("/Users/IggyMac/OneDrive - UvA/VU work/Example SQL databases/CoronaImpact/Yuth unemployement/estat_ei_lmhr_m.tsv", sep='\t')

data = data.reset_index()
data = data.rename(columns={"index": "geo_id"})
country_list = []
country_names = pd.read_csv("/Users/IggyMac/OneDrive - UvA/VU work/Example SQL databases/CoronaImpact/CountryTable/countryabbrv.txt")

for index, row in data.iterrows():
    country = row[data.columns[1]][(row[data.columns[1]]).rfind(",")+1:]
    country_list.append(country)

data["name"] = country_list

country_id_df = data[["geo_id", "name"]]
country_id_df = country_id_df.rename(columns={"name": "abbrv"})
country_id_df = pd.merge(country_id_df, country_names, left_on = "abbrv", right_on = "Code", how = "left")
country_id_df.to_csv("//Users/IggyMac/OneDrive - UvA/VU work/Example SQL databases/CoronaImpact/CountryTable/geos.csv")