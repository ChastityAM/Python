employees = {}
while True:
    try:
        add_employees = int(input("How many employees would you like to enter? \n"))
        entries = add_employees
        if (add_employees < 1): 
            raise Exception
    except ValueError:
        print("Please enter a number of entries.")
    else:
        print("Let's get started then")
        break
i = 0
while i < entries:
    employee = {
        "Name ": "",
        "Age " : 0,
        "Email " : ""
    }
    
    name = input("Enter first and last name. \n").split(" ")
    employee["name"] = name

    while True:
        try:
            age = int(input("Please enter employee age. \n"))
            if age <= 15:
                print("Employee must be at least 15!")
                continue
        except ValueError:
            print("Please enter a number.\n")
        else:
            employee["age"] = age
            break
    employee["email"] = name.replace(" ",".".lower) + "@company.com"    
    employees.append(employee)
    i += 1

print(employees)
