import os
csvpath = os.path.join('Resources', 'accounting.csv')

import csv
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    for row in csvreader:
        print(row)