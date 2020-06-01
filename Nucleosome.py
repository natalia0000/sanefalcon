
"""
Nucleosome script can be used to combine upstreamProfs.csv and downstreamProfs.csv
"""


import pandas as pd
import csv

with open("upstreamProfs.csv") as f:
    reader = csv.reader(f)
    data_up = []
    for row in reader:
        data_up.append(row)

with open('downstreamProfs.csv') as f:
    reader = csv.reader(f)
    data_down = []
    for row in reader:
        data_down.append(row)

data_up.sort()
data_down.sort()
data_all = []
for index_sample in range(len(data_up)):
    new_row = data_up[index_sample][2:-1]
    new_row.append(data_up[index_sample][0])
    new_row.reverse()
    new_row.extend(data_down[index_sample][1:])
    data_all.append(new_row)

df = pd.DataFrame(data_all)
df.to_csv(r'streamProfs.csv', header=False, index=False)

