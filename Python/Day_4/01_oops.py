# OOP in Python

'''

Class = a blueprint (it defines what data an object has and what it can do).
Object = a thing made from that blueprint (an instance with real values).

'''

# Simple class

class Hello:
    pass

c = Hello()
print(c)

# Add data with __init__ (the constructor)

'''
Note: The constructor is a special method that is called when an object is created.
      It is used to initialize the object's data.
      self refers to the object itself.
'''

class Person:
    def __init__(self, name, job, age):
        self.Person_name = name
        self.Person_job = job
        self.Person_age = age
        
p = Person("Sai", "Developer", 24)
print(p.Person_name)
print(p.Person_job)
print(p.Person_age)

# Add methods and Default values
'''
Note : All required non deault parameters should comes before the default parameters.
'''

class Employee:
    def __init__(self, name, age, job = "SDE"):
        self.Employee_name = name
        self.Employee_job = job
        self.Employee_age = age
    
    def salary(self, amount):
        print(f"Salary for {self.Employee_name} is {amount} with {self.Employee_job}")

    def experience(self, years):
        return (f"{self.Employee_name} has {years} years of experience")
    
e = Employee("Sai", 24)
e.salary(5000)
print(e.experience(5))


# Shared Attributes and adding Attributes
'''
Note: Shared attributes are attributes that are common to all instances of a class.
      Adding attributes to a class adds them to all instances of that class.
'''

class Player:
    player = "sportsman"
    def __init__(self, sports, name, salary):
        self.sports = sports
        self.name = name
        self.salary = salary

    def updated_salary(self, amount):
        self.salary += amount
        print(f"Salary updated to {self.salary} with incease of {amount}")

p1 = Player("cricket", "Sai", 30000)
p2 = Player("football", "Sai", 50000)

print(p1.player)

p2.updated_salary(60000)

p1.bike = "mountainbike"
print(p1.bike)