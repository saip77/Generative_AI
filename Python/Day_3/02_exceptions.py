#Basic Exceptions

try:
    x = int("abc")  # error
except:
    print("Something went wrong!")

try:
    num = 10 / 0
except ZeroDivisionError:
    print("You cannot divide by zero!")


try:
    f = open("test.txt")
    print("File opened")
except FileNotFoundError:
    print("File not found!")
finally:
    print("This runs no matter what")
