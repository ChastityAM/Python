x = 10
y = 10
print(x == y)
print(x is y)
str1 = "Hello"
str2 = "Hello"
print(str1 == str2)
print(str1 is str2)
list1 = [1, 2, 3] #these have the same values, but are
list2 = [1, 2, 3] # 2 different objects
print(list1 is list2) #checks if they are the same object(identity)
print(list1 == list2) #checks if values are same

print(type("Hello") is str) #check class
print("Hello" is not "World")
