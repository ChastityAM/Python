continue_asking = True
while continue_asking == True:
    asking = str(input("Would you like to ask about a year?"))
    if asking == "yes":    
        year = int(input("Enter a year: "))  
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
    else:
        print("Okay, have a nice day!")
        break

