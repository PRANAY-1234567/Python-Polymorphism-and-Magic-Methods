# Duck Type - 
# It is a type of philosapy in python 
# it will focus on behaviour no need to focus on Object
# It will work without using Inheritance


'''class Dog:
    def sound(self):
        print("Bark....")

class cat:
    def sound(self):
        print("Meow...")
class Goat:
    def sound(self):
        print("Goat")

def animal(x):
    x.sound()

animal(Dog())
animal(cat())
animal(Goat())'''


#By the Help Of Looping
class Bike:
    def start(self):
        print("Bike Started")

class Class:
    def start (self):
        print("Class Started")

class Car:
    def start(self):
        print("Car Started")

class Engine:
    def start (self):
        print("Engine Started")

w = [Bike(), Class(), Car(), Engine()]

for i in w:
    i.start()