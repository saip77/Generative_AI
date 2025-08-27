#Shopping Cart System 🛒

'''
Input items into a list until user types "done".

Print the final shopping cart.
'''

items = []

while True:
    item = input("Enter item: ")
    if(item == "done"):
        break
    else:
        items.append(item)

print(items)