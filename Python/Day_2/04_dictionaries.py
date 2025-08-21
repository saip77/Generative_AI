# empty dictionary
dict1 = {}

# normal dictionary
student = {
    "name": "Alice",
    "age": 21,
    "subjects": ["Math", "Science"]
}

print(student)


print(student["name"])   # Alice
print(student.get("age")) # 21
print(student.get("grade", "N/A"))  # safe access, returns "N/A" if key not found


#Upadating dictionary
student["age"] = 22       # update
student["city"] = "Paris" # add new key-value
print(student)


student.pop("city")   # removes key, returns its value
print(student)

del student["age"]    # removes key
print(student)


#Methods

student = {"name": "Alice", "age": 21, "city": "Paris"}

print(student.keys())    # dict_keys(['name', 'age', 'city'])
print(student.values())  # dict_values(['Alice', 21, 'Paris'])
print(student.items())   # dict_items([('name', 'Alice'), ('age', 21), ('city', 'Paris')])

for key, value in student.items():
    print(key, ":", value)
