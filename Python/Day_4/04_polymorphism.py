# Polymorphism

'''
Polymorphism means “many forms” — the same operation or method can behave differently 
depending on the object that calls it.
'''

# Example of Polymorphism
class Animal:
    def __init__(self, name):
        self.name = name
    
    def sound(self):
        print(f"Animal {self.name} makes a sound")
    
class Dog(Animal):
    def sound(self):
        print(f"Dog {self.name} barks")
    
class Cat(Animal):
    def sound(self):
        print(f"Cat {self.name} meows")

a = Animal("Lion")
a.sound()

d = Dog("Tom")
d.sound()

c = Cat("Billu")
c.sound()