#Electricity Bill Calculator

'''Input number of units consumed.
First 100 units = ₹5/unit, next 100 = ₹7/unit, above 200 = ₹10/unit.
Print total bill.
'''

units = int(input("Enter number of units consumed: "))

bill = 0

if units >0 and units < 100:
    bill = units * 5
elif units >= 100 and units < 200:
    bill = 100 * 5 + (units - 100) * 7
elif units > 200:
    bill = (units % 100)* 10 +  100*7 + 100*5
else:
    print("Invalid input")

print(f"Total bill: Rs.{bill:.2f}")