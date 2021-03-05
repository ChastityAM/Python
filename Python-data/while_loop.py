fruits = ["apple", "orange", "banana", "cherry", "kiwi"]
while fruits: print(fruits.pop(0))
else: print("fruits have resolved to False")
print(f"loop ended, fruits = {fruits}")

i = 0 
while i < 10:
    i =+ 1
    if (i % 2 == 0):
        continue
    if (i == 7):
        break
    print(i)
else:
    print("The number has finished counting")