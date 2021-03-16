import csv
import json

cols = []
rows = []
with open("data.csv", "rt") as csvfile:
    data = csv.reader(csvfile) 
    cols = next(data)
    for row in data:
        rows.append(row)

print("Headers: ", cols)
for row in rows:
    print(row)

csvdata = []

with open("data.csv", "rt") as csvfile:
    data = csv.reader(csvfile) 
    cols = next(data)
    print(cols)
    for row in data:
        instance = {}
        for i in range(len(cols)):
            instance[cols[i]] = row[i]
        csvdata.append(instance)
print("List of dictionaries: ")
for entry in csvdata:
    print(entry)

print(type(csvdata))
print(type(json.dumps(csvdata)))
with open("data.json", "wt") as data:
    data.write(json.dumps(csvdata, indent=2))
    
print(data)

