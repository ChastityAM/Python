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
#what will x print 
x=0
while(x<100):
    x+=2
    print(x)
print("------------------------")

#MAKE FOR AND WHILE LOOP IN RANGE TO PRINT 1-7
for i in range(1, 8):
    print(i)
print()

j = 1
while j <= 7:
    print(j)
    j += 1

