#Discount Price Calculator

'''Input original price and discount percentage.
Print the final price after discount.
'''

original_price = float(input("Enter original price: "))
discount_percentage = float(input("Enter discount percentage: "))

final_price = original_price - (discount_percentage/100)*original_price

print(f"Final price after discount: Rs.{final_price:.2f}")