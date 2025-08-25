#Student Grade Report

'''Input student name and marks in 3 subjects.
Print the total marks, average, and percentage in a neat format.
'''

name = input("Enter student name: ")

maths = float(input("Enter marks in Maths: "))
science = float(input("Enter marks in Science: "))
english = float(input("Enter marks in English: "))

total_marks = maths + science + english
average_marks = total_marks / 3
percentage = (maths + science + english) / 300 * 100

print(f"Name: {name}")
print(f"Total Marks: {total_marks:.2f}")
print(f"Average Marks: {average_marks:.2f}")
print(f"Percentage: {percentage:.2f}%")