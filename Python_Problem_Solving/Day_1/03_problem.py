#Fuel Cost Estimator

'''
Input distance (km) and mileage of your car (km/l).
Input petrol price per liter.
Calculate and print the total cost of fuel for the trip.
'''

distance = float(input("Enter the distance traveled (km): "))
mileage = float(input("Enter the mileage of your car (km/l): "))
petrol_price = float(input("Enter the petrol price per liter: "))

fuel_cost = (distance/mileage) * petrol_price

print(f"Total cost of fuel: ${fuel_cost:.2f}")