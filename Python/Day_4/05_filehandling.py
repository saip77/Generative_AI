# File Handling

'''
File Handling in Python is done using the open() function.

open() function takes two arguments:
1. File name
2. Mode
'''

# Reading a file
file = open("file.txt", "r")
print(file.read())
file.close()

# Writing to a file
file = open("file.txt", "w")
file.write("Hello World!")
file.close()

# Appending to a file
file = open("file.txt", "a")
file.write("Hello Again!")
file.close()

# Reading a file line by line
file = open("file.txt", "r")
for line in file:
    print(line)
file.close()

# Reading a file line by line (using while loop)
file = open("file.txt", "r")
line = file.readline()
while line:
    print(line)
    line = file.readline()