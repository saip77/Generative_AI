# Operators in Python

# Arithmetic Operators

x = 10
y = 3

print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Floor Division:", x // y)
print("Modulus:", x % y)
print("Exponentiation:", x ** y)

# Comparison Operators

x = 10
y = 3

print("Equal to:", x == y)
print("Not equal to:", x != y)
print("Greater than:", x > y)
print("Less than:", x < y)
print("Greater than or equal to:", x >= y)
print("Less than or equal to:", x <= y)

# Logical Operators

"""
Note: In Python 1 2 3 "hi" [1,2,3] are all True
      where as 0, " ", None, [] are all False
"""
x = True
y = True

print("And:", x and y)
print("Or:", x or y)
print("Not:", not x)

# Membership Operators

fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3]

print(3 in numbers)
print(5 in numbers)

print("apple" in fruits)
print("orange" in fruits)