#Grocery Bill Calculator

'''Input price of 3 grocery items.
Print the total bill and also the average cost per item. '''

item_1 = float(input("Price of item 1: "))
item_2 = float(input("Price of item 2: "))
item_3 = float(input("Price of item 3: "))

total = item_1 + item_2 + item_3

average_price = total / 3

print(f"Total Bill: Rs.{total:.2f}")
print(f"Average Price per Item: ${average_price:.2f}")