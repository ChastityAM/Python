try:
    num = int(input("Please enter an integer.\n"))
    if (num ==3):
        div = 10 / int(num)
except ValueError:
    print("You didn't enter a value that can be used")
except ZeroDivisionError:
    print("Please don't divide by zero")
except Exception:
    print("General Exception")
else:
    print(f"10 / {num} = {div}")
finally:
    print("This will always execute")
while True:
    try:
        age = int(input("enter your age: "))
        print(f"Ok, you are {age} years old")
        if (age < 15):
            raise Exception
    except Exception:
            print("You're too young to drive!")
            break
    except ValueError:
        print("Please enter a number.")
    else:
            print(f"Ok! You can take the test!")
            break

print("End of program.")