def weird_arithmetic(x, y, z): #function defined
    print((x**x + y**z) // z)  #code block

weird_arithmetic(5, 6, 7) #function called

def greeting(a, b):
    print(a + b + "!")

greeting("Hello ", "Bethany")

def my_sum(n1, n2):
    return n1 + n2

some_number=my_sum(8, 3)

print(some_number)

def area(a, b):
    return a * (b**2)
c_area=area(3.14, 4)

print(c_area)

def volume(c_area, height):
    return(c_area * height)

cylinder=volume(c_area, 10)

print(cylinder)
