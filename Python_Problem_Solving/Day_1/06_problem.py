#Salary Slip Generator

'''Input employee name, base salary.
Assume HRA = 20% of base, DA = 10% of base.
Print the gross salary with an f-string.
'''

employee_name = input("Enter employee name: ")
base_salary = float(input("Enter base salary: "))

hra = base_salary * .2
daa = base_salary * .1

gross_salary = base_salary + hra + daa

print(f"Gross Salary for {employee_name}: ${gross_salary:.2f}")