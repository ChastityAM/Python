ride_type = "Dryft"
credits = 4

ride_price = 0
final_price = 0

if ride_type == "Oober":
    ride_price = 20.5
elif ride_type == "Dryft":
    ride_price = 38.4
else:
    ride_price = 18.9

print("Ride price:")
print(ride_price)

if credits > 0:
    final_price = ride_price - credits

print("Final Price:")
print(final_price)

