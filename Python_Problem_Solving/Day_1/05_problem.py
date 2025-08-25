#BMI Calculator

'''Input weight (kg) and height (m).
Calculate BMI = weight / height².
Print result as: "Your BMI is 23.5"
'''

weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

bmi = weight / (height **2)

print(f"Your BMI is {bmi:.2f}")