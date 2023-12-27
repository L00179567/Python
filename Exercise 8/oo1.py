#####################
Anatomy of a simple class
By: Sai Mahesh
11 DEC 2023
#############


class Buffalo:
    # Class variable
    species = "Murray"

    # Constructor (initializer) method
    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age

    # Instance method
    def bark(self):
        print("booo!")

    # Another instance method
    def describe(self):
        print(f"{self.name} is {self.age} years old.")

# Creating an instance of the Buffalo class
my_buffalo = Buffalo(name="Sultan", age=9)

# Accessing instance variables
print(f"{my_buffalo.name} is a {my_buffalo.species}")

# Calling instance methods
my_buffalo.bark()
my_buffalo.describe()

