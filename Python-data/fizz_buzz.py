num = int(input("Please enter a number higher than 1 \n"))
list = []
for i in range(1, num + 1):
        if (i==num):
            break
        if i % 3 == 0 and i % 5 == 0:
            list.append("Fizzbuzz")
        elif i % 3 == 0:
            list.append("Fizz")
        elif i % 5 == 0:
            list.append("Buzz")   
        else:
            list.append(i) 

sum = 0
for item in list:
    print(item)
    if type(item) == int:
        sum += item

print("Sum of integers: ", sum)
print("Count of Fizzbuzz: ", list.count("Fizzbuzz"))
print("Count of Fizz: ", list.count("Fizz"))
print("Count of Buzz: ", list.count("Buzz"))
       

