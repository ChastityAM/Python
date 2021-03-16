import json

from_json = []
with open("data.json","rt") as data:
    from_json = json.loads(data.read())
for entry in from_json:
    for key, value in entry.keys():
        print(str(key) + ": " + str(key))
    
