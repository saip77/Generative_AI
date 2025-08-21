set1 = {1, 2, 3, 4, 5}
set2 = {"hello", "world", "python", "programming"}
set3 = {1, 2, 3, 4, 5, "hello", "world", "python", "programming"}

print(set1)

set1.add(6)
print(set1)

set1.remove(6)
print(set1)


set1_copy = set1.copy()
print(set1_copy)

print(set1.difference(set2))
print(set1.intersection(set2))
print(set1.isdisjoint(set2))
print(set1.issubset(set2))
print(set1.issuperset(set2))
print(set1.union(set2))



fruits = {"apple", "banana"}

fruits.add("cherry")   # add single element
print(fruits)

fruits.update(["mango", "kiwi"])  # add multiple
print(fruits)

fruits.remove("banana")  # remove item (❌ error if not found)
print(fruits)

fruits.discard("orange") # remove item (✅ no error if not found)
print(fruits)

x = fruits.pop()   # removes a random element
print(x, fruits)

fruits.clear()     # empty the set
print(fruits)      # set()
