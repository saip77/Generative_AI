#Simple list
fruits = ["apple", "banana", "cherry", "mango", "orange", "pineapple"]
print(fruits)

#Mixed list
mixed_list = [1, "hello", True, None, fruits]
print(mixed_list)


#Nested list
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list[0][1])


#Accessing list elements
print(fruits[0])
print(fruits[-1])   # last element
print(fruits[1:-1]) # elements from index 1 to last index excluding last index
print(fruits[:-1])  # elements from index 0 to last index excluding last index
print(fruits[1:])   # elements from index 1 to last index
print(fruits[1: 3]) # elements from index 1 to index 3 exclding index 3


#Changing list elements
fruits[0] = "guava"
print(fruits)


#Adding elements
fruits.append("papaya")   # add at the end
fruits.insert(2, "kiwi")  # add at index 2
fruits.extend(["dragonfruit", "jackfruit"]) # add at the end
print(fruits)


#Removing elements
del fruits[0] # remove first element
del fruits[-1] # remove last element
del fruits[1:3] # remove elements from index 1 to last index excluding 3rd index
fruits.pop() # remove last element
fruits.pop(2) # remove element at index 2
print(fruits)


#Useful list methods
fruits.sort() # sort list in ascending order
print(fruits)
fruits.reverse() # reverse list
print(fruits)
print(len(fruits)) # length of list
print(fruits.index("mango")) # index of element


#Looping through list
for fruit in fruits:    
    print(fruit)