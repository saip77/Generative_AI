#Currency Converter

'''
Input amount in USD.
Convert to INR (assume 1 USD = 83 INR).
Print the result.
'''
amount = float(input("Enter amount in USD: "))

inr = amount * 83

print(f"Amount in INR: Rs.{inr:.2f}")
