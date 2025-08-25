#Restaurant Bill Splitter

'''Input total bill amount and number of friends.
Print amount each person has to pay (use division operator).
'''

total_bill = float(input("ENter total bill:"))
friends = int(input("Enter number of friends:"))

bill_per_person = total_bill / friends

print(f"Amount each person has to pay: ${bill_per_person:.2f}")