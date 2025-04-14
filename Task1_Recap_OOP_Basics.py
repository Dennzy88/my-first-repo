"""
Write a Python class called Person that:

Has an attribute name

Has a method greet() that prints: "Hello, my name is [name]!"

Then:

Create an instance of Person

Call the greet() method
"""

class Person:
    def __init__(self, name):
        self.name = name
        
    def greet(self):
        print(f"Hello, my name is {self.name}!")
        
# Create an instance of Person
person = Person("Dennzy")

# Call the greet() method
person.greet()
