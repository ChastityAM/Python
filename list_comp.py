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
def square(x):
    return x**2
print("--------------------------")
#lambda function to do same squaring
print(list(map(lambda x: x**2, 1)))


