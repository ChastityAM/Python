class Car():
    
    #automatically setting these
    wheels = 4
    doors = True

    def __init__(self, color, make, year, HP):
        self.color = color #attributes
        self.make = make
        self.year = year
        self.HP = HP
# method 1
    def start_car(self):
        print("Veroom")
# compares which one is greater by comparing HP
    def __gt__(self, other):
        return self.HP > other.HP

my_car = Car("blue", "Ford", 2020, 150)
your_car = Car("red", "Tesla", 2020, 200)

my_car.start_car()

print(my_car < your_car)
print (my_car <= your_car)