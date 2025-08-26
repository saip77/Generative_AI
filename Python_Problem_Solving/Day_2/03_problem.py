#Movie Ticket Booking 🎬

'''
Input age and time of show.
Ticket Price:
Kids (<12) → ₹100
Adults (12–60) → ₹200
Seniors (60+) → ₹150

If show is after 6 PM → add ₹50 surcharge.
'''

age = int(input("Enter age: "))
show_time = int(input("Enter show time (in hours): "))
price = 0
extra_charge = 0
if(show_time > 18):
    extra_charge = 50
if(age < 12):
    price = 100
elif(age >= 12 and age <= 60):
    price = 200
else:
    price = 150

total_price = price + extra_charge
print(f"Total price: Rs.{total_price:.2f}")