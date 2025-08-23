# Inheritence

'''
Inheritence is a mechanism that allows a class to inherit the attributes and methods of another class.
It is a way of reusing code and reducing duplication.
'''

# Example of Inheritence
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self,name, sound):
        self.sound = sound
        super().__init__(name)   # call Animal's __init__


    def details(self):
        print(f"Name: {self.name}, Sound: {self.sound}")

class Cat(Animal):
    def meow(self):
        print(f"Meow! My name is {self.name}")

c = Cat("Billu")
c.meow()
d = Dog("Tom", "woof")
d.details()