#ATM Withdrawal Simulation 🏦

'''User enters amount to withdraw.
Rules:
Only multiples of 100 allowed.
Must not exceed balance.
Print remaining balance or error message.
'''

balance = 1000

amount = int(input("Enter amount to withdraw: "))

if(amount % 100 == 0):
    if(amount <= balance):
        balance -= amount
        print(f"Remaining balance: ${balance:.2f}")
    else:
        print("Insufficient funds")
else:
    print("Invalid amount")