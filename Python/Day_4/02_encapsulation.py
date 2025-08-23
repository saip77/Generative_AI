# Encapsulation

'''
Encapuslation means bundling data(attributes) and methods(functions) together in a class,
while also controlling how that data is accessed or modified.
'''

# Private attributes
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return (f"Name: {self.__name} Age: {self.__age}")
    
p = Person("Sai", 24)
print(p.get_name())


# Getter and Setter
class Employee:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        
    #getter
    def get_name(self):
        return (self.__name + " is " + str(self.__age) + " years old")
    
    #setter
    def set_age(self, age):
        self.__age = age
        
e = Employee("Sai", 23)
print(e.get_name())
e.set_age(24)
print(e.get_name())
e.age = 25    # this just creates a new attribute, doesn't affect __age
print(e.get_name())
e._Employee__age = 26   # directly modifies the private variable but not recommended
print(e.get_name())