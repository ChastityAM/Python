list_of_nums = [0, 1, 2, 3, 4, 5]

#for loop
for elem in list_of_nums:
    if type(elem) == str:
        continue
    print(elem)
print("------------------------")

#range loop
for i in range(10):#prints 1 through 9
    print(i)
print("------------------------")

for i in range(4, 20,2):#prints 4 through 20 counting by 2's
    print(i)
print("------------------------")

#while loop
i=0
while i < 10:
    print(i)
    i += 1
print("------------------------")
i = 0
while True:
    i += 1
    print(i)
    if i > 10:
        break
print("------------------------")

for i in range(10):#prints 1 through 9
    print(i)
print("------------------------")
x=0
while(x<100):
    x+=2
    print(x)
print("------------------------")

#list_of_numbers = [1, 2, 3, 4, 6, 8, 11, 18, 20]
n = int(input("Please enter a number: "))
while True:
    if n % 2 != 0:
        print("Weird")
    elif n >= 2 and n <= 5 and n % 2 == 0:
        print("Not Weird")
    elif n >= 6 and n <= 20 and n % 2 == 0:
        print("Weird")
    break
   
