h = 10

def area(r):
    return 3.14*r**2

c_area = area(4)

def volume(c_area, h):
    vol = c_area*h
    print("Area is", c_area, "and volume is", vol)

volume(c_area, h)

