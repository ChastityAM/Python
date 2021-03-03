try:
    user_int = int(input("Please enter an integer."))
    a = 1/0
    import I_dont_exist
except ValueError:
    print("You didn't enter a value that can be used")
except ZeroDivisionError:
    print("Please don't divide by zero")
except Exception:
    print("General Exception")

print("End of program.")

n = 2
if n < 5:
    raise Exception
print("End of program.")