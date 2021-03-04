from typing import FrozenSet


tup = (1, 2, 3)
print(type(tup))

output = tup[2]
print(output)

fruits = ("apple", "blueberry", "cherry", "apple", "mango", "banana")
print(fruits[2])
print(fruits[-1])
print(fruits[1:3])
#cannot reassign or add things in this because it's a tuple
apple_count = fruits.count("apple")
print(apple_count)
apple_index = fruits.index("apple")
print(apple_index)
#to add to a tuple, make a new list and add to past list
new_tuple = ("pineapple", "guava", "starfruit")
fruity = fruits + new_tuple
print(fruity)

set_of_unique_numbers = set([1,1,1,2,2,3,3,3,4,4,5,6,7])
print (set_of_unique_numbers)

fruits = {"apple", "blueberry", "cherry", "pineapple", "mango"}
fruits.add("banana")
print(fruits)
fruits.add("cherry") #won't add a dupe, but won't error either
print(fruits)
fruits.remove("apple")
print(fruits)

winter_fruits = {"grapefruit", "oranges", "tangerines"}
fruits_liked = {"tangerines", "apples", "kiwi", "oranges"}
#elems in both
intersection = fruits_liked.intersection(winter_fruits)
print(intersection)
#all unique elems from each set
union = fruits_liked.union(winter_fruits)
print(union)
#whether it's a superset of given set (everything is included)
favs = fruits_liked.issuperset(winter_fruits)
print(favs)

difference = winter_fruits.difference(fruits_liked)
print(difference)
#make a set that you cannot alter, will print in random order
frozen_set = frozenset(["apple", "cherry", "banana"])
print(frozen_set)
print(frozen_set.union(fruits_liked))
