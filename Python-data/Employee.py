employee_name = input("Enter first and last name. \n").split(" ")
first_name = employee_name[0].capitalize()
last_name = employee_name[1].capitalize()

employee_age = input("Please enter your age. \n")
age = int(employee_age)

employee_email = f'{first_name.lower()} . {last_name.lower()} {"@company.com"}'
print(
f"""
Name: {employee_name}
Age: {employee_age}
Email: {employee_email}
"""
)