list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8]

a = list_of_numbers[5] #selecting an index
b = list_of_numbers[2:5] #slicing the list
                #doesn't include last index given in printout

print(a)
print(b)
list_of_numbers[5] = 77
list_of_numbers.append(10)
list_of_numbers.pop(4) #removes at this index, if not indicated, will remove last one
list_of_numbers.reverse()

print(list_of_numbers)


fruits = ["apple", "blueberry", "cherry", "mango", "banana"]
print(fruits)
fruits[3] = "pineapple" #reassigning slot 3
print(fruits)
first_element = fruits[0]
print(first_element)
last_element = fruits[-1]
print(last_element)

print(len(fruits))

fruits.insert(2, "guava")#add to list at the index you chose
print(fruits)