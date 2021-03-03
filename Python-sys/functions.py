def weird_arithmetic(x, y, z): #function defined
    print((x**x + y**z) // z)  #code block

weird_arithmetic(5, 6, 7) #function called

def greet_friend(greeting, name):
    print(greeting, name + "!")

greet_friend("Hello", "Bethany")

def my_sum(n1, n2):
    return n1 + n2

some_number=my_sum(8, 3)

print(some_number)

def area(a, b):
    return a * b ** 2
c_area=area(3.14, 4)

print(c_area)

def volume(c_area, height):
    print(c_area * height)

volume(c_area, 10)

def friend_greets(name, greeting, sentence):
    output = "{0},{1}! {2}".format(greeting, name, sentence)
    print(output)

friend_greets("John", "Hey", "How you doin?")

def greet_user(greeting):
    user = input("Please enter your name.\n")
    print("{},{}!".format(greeting, user))

    print(5 + int(input("Please enter an integer.")))
greet_user("Hello")