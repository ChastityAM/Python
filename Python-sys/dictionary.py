dict_of_names = {'Yellow':"Kalina", 'Black':"Nika", 'Pink':"Phineas"}

name = dict_of_names['Pink']
print(name)

values = dict_of_names.values()
keys = dict_of_names.keys()

items = dict_of_names.items()

print(list(values))
print(list(keys))
print(list(items))

user = {
    "username" : "Hello",
    "password" : "world@1",
    1 : True,
    "user id" : 123,
    "friend_id" : [456,123],
}

print(user["username"])
print(user["password"])
user["friend_id"] = [456,123,789]
print(user)
user["status"] = {
    "active" : True,
    "banned" : False
}
print(user["status"])

new_dictionary = dict.fromkeys({"Hello", "World", "Python"})
print(new_dictionary)