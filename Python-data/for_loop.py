fruits = ["apple", "orange", "banana", "cherry", "kiwi"]

for fruit in fruits:
    print(fruit)

word = "Groot"

for letter in word:
    print(letter)

user = {
    "name" : "Peter",
    "password" : "Starlord",
    "id" : 1980
}

for key in user:
    print(key)

for key in user:
    print(f"{key}:{user[key]}")
#or
for key,value in user.items():
    print(f"{key}: {value}")

key_set = {"fruit", "vegetable", "meat"}

for key in key_set:
    print(key)