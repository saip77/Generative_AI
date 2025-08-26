#Input hours parked.

'''Charges:
First 2 hours = ₹20/hr
Next 3 hours = ₹50/hr
Above 5 hours = ₹100/hr
Print total fee.
'''

total_hours = int(input("Enter total hours parked: "))
fee = 0
if(total_hours <= 2):
    fee = total_hours * 20
elif(total_hours > 2 and total_hours <= 5):
    fee = 2*20 + (total_hours-2)*50
else:
    fee = 2*20 + 3*50 + (total_hours-5)*100
    
print(f"Total fee: Rs.{fee:.2f}")