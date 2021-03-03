def is_leap_year(year):
    if (year % 4) == 0:  
        if (year % 100) == 0:  
            if (year % 400) == 0:  
                print("{0} is a leap year".format(year))  
            else:  
                print("{0} is not a leap year".format(year))  
        else:  
            print("{0} is a leap year".format(year))  
    else:  
        print("{0} is not a leap year".format(year))

if __name__ == "__main__":
    continue_asking = True
    while continue_asking == True:
        asking = str(input("Would you like to ask about a year?\n"))
        if asking == "yes":    
                year = int(input("Enter a year: \n"))  
                is_leap_year(year)
        else:
                print("Okay, have a nice day!")
                break