list_nums = [1, 2, 3, 4, 5, 6, 7, 8]

for elem in list_nums:
    if elem >= 5:
        print(elem)
print("--------------------------")
#list comprehension
[print(elem) for elem in list_nums if elem >= 5]
#this is a generator 
#(print(elem) for elem in list_nums if elem >= 5)

print("--------------------------")
#squaring function
x = 4
def square(x):
    return x**2
print("--------------------------")
#lambda function to do same squaring
#print(list(map(lambda x: x**2, 1)))

fruits = ["apple", "grape", "banana", "starfruit", "kiwi", "dragonfruit", "pineapple"]
long_fruits = [fruit for fruit in fruits if len(fruit) > 6]
long_fruits = [fruit.capitalize() for fruit in fruits if len(fruit) > 6]
long_fruits = [f"A delicios {fruit}" for fruit in fruits if len(fruit) > 6]

print(long_fruits)