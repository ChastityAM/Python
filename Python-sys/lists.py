list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8]

a = list_of_numbers[5] #selecting an index
b = list_of_numbers[2:5] #slicing the list
                #doesn't include last index given in printout

print(a)
print(b)
list_of_numbers[5] = 77
list_of_numbers.append(10)
list_of_numbers.pop(4)
list_of_numbers.reverse()

print(list_of_numbers)