import csv
from collections import namedtuple

with open('stock.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        print(row)
    
    print(row[0])
    print(row[1])
    print(row[5])
    
    f.close()