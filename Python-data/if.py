x = int(input("Enter a number: \n"))
#ternanry operators (conditional expressions)
message = "Greater than 10" if (x > 10) else "10 or less"
print("Greater than 10") if (x > 10) else print("10 or less")

if x: print("You entered something")
elif (x == None): print("You entered a None somehow")
else : print("You didn't enter anything")

if (x > 10):
    print("You enter a number greater than 10")
    y = 3
    if x % 2 == 0:
        print("and it's even!")
elif (x < 10):
    print("You entered a number less than 10")
