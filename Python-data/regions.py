# add up each instance of a,b,c,d,e,f and give rankings
# each region do same 

import csv

headers = []
candidates = ["A", "B", "C", "D", "E", "F"]
national = dict.fromkeys(candidates, 0)
north = dict.fromkeys(candidates, 0)
south = dict.fromkeys(candidates, 0)
east = dict.fromkeys(candidates, 0)
west = dict.fromkeys(candidates, 0)
central = dict.fromkeys(candidates, 0)

with open("votes.csv", "rt") as csvfile:
    data = csv.reader(csvfile)
    headers = next(data)
    for row in data:
        national[row[3]] += 1
        if row[1] == "NORTH" : north [row[2]] +=1
        elif row[1] == "SOUTH" : south [row[2]] +=1
        elif row[1] == "EAST" : east [row[2]] +=1
        elif row[1] == "WEST" : west [row[2]] +=1
        elif row[1] == "CENTRAL" : central [row[2]] +=1

national_winner = max(national, key=national.get)
north_winner = max(north, key=north.get)
south_winner = max(south, key=south.get)
east_winner = max(east, key=east.get)
west_winner = max(west, key=west.get)
central_winner = max(central, key=central.get)

print("national", national, national_winner)
print("NORTH", north, north_winner)
print("SOUTH", south, south_winner)
print("EAST", east, east_winner)
print ("CENTRAL", central, central_winner)

