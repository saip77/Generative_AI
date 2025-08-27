#Marks Analyzer 📊

'''
Store marks of 5 subjects in a list.
Calculate total, average, highest, and lowest marks.
'''

marks = []

for i in range (1, 6):
    input_marks = float(input(f"Enter marks for subject {i}: "))
    marks.append(input_marks)

total = 0
for i in range(len(marks)):
    total += marks[i]

average = total / len(marks)

marks.sort()
highest = marks[-1]
lowest = marks[0]

print(f"Total: {total:.2f}")
print(f"Average: {average:.2f}")
print(f"Highest: {highest:.2f}")    
print(f"Lowest: {lowest:.2f}")