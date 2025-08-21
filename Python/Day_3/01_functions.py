#Defining and calling functions
def add(x, y):
    return x + y

result = add(2, 3)
print(result)

# Default arguments
def add(x, y=0):
    return x + y
result = add(2, 3)
print(result)
result = add(2)
print(result)

#Keyword arguments
def student(name, age):
    print(f"Name: {name}, Age: {age}")

student(age=21, name="Alice")  # order doesn’t matter
