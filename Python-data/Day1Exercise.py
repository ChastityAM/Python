''' Prompt user for name, age and years coding keys
store as dictionary 
prompt user to enter first 3 programming languages
store them as tuple. 
Prompt user to give fav 3 languages
store them as a list. 
Create a set that is an intersection of the 2
Add all of these collections as keys to the dictionary
format print statement to print relevant data'''

user = {
    "name" : None,
    "age" : None, 
    "years_coding" : None,
}

user["name"] = input("Enter your name: \n")
user["age"] = input("Enter your age: \n")
user["years_coding"] = input("How many years have you been coding? \n")
print(user)

first_languages = input("Enter your first 3 programming languages with spaces between. \n")
lang_list = first_languages.split(" ")
lang_tuple = tuple(lang_list)
user["first_languages"] = lang_tuple

fav_languages = input("Enter your 3 fav programming languages with spaces between. \n")
fav_list = fav_languages.split(" ")
user["fav_lanuages"] = fav_list
first_set = set(lang_list)
fav_set = set(fav_list)
consistant_fav = first_set. intersection(fav_set)
print(consistant_fav)
