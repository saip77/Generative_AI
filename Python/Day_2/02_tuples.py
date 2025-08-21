#Empty tuple
empty_tuple = ()
print(empty_tuple)

#Single element tuple must use comma
single_tuple = ("hello",)
print(single_tuple)

#Tuple with multiple elements
multiple_tuple = ("hello", 1, True, None)
print(multiple_tuple)

#Tuple with nested elements
nested_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(nested_tuple[0][1])



#Accessing tuple elements
colors = ("red", "green", "blue", "yellow", "orange")
print(colors[0]) # first element
print(colors[-1]) # last element
print(colors[1:-1]) # elements from index 1 to last index excluding last index



#Immutable tuple
colors = ("red", "green", "blue", "yellow", "orange")    
# colors[0] = "pink" # error



#Tuple methods
nums = (1, 2, 2, 3, 4)

print(nums.count(2))   # 2 (how many times value appears)
print(nums.index(3))   # 3 (first index of value 3)



#Packing unpacking
person = ("Sai", 21, "Hyderabad")

name, age, city = person
print(name)  # Sai
print(age)   # 21
print(city)  # Hyderabad
