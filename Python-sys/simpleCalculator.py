 #This will take input from the user
a = int(input("Please enter a number: "))
b = int(input("Please enter another number. NOT ZERO: "))
#This will add 
def add(a, b):
    sum = a + b
    return sum
#This will subtract
def sub(a, b):
    dif = a - b
    return dif
     
sum = add(a, b)
dif = sub(a, b)
#This will print the lines you wanna see 
print("The sum of your two numbers is", sum)
print("The difference of your two numbers is", dif)

