"""
# What is oops?
    object-oriented programing language that creates an object and classes, reuse of an object and classes throughout the program.

    object has attribute and behaviour, to store data in variable and create a methods/function
    Attributes: every data is stored inn variable (eg: height, weight, working company details)
    Behaviour: action or doing (eg: iam walking, running, sleeping)

    class - designing of the object,
    object - Instance of class

    Eg: This phone is designed by Motorola is class
        This phone is manufactured by china is object

    class has special methods or constructor called __init__ to getting input from user or default value

    class has two types of variable:
        * Class variable (creating a variable under the class name)
        * Instance variable (creating a variable inside the methods)

    class has three types of methods:
        * Instance methods(to create a methods for getting and setting the value)
        * static methods(to create a methods for using class variable)
        * class methods(to create a class for doing extra things not using any values in it)

    Concepts of Oops:
        * Inheritance
        * Encapsulation
        * Polymorphism
        * Data abstraction
"""

# creating class using keyword class and assign a name to that class
class Laptop:

    # class/static variable
    battery = "100 wh"

    # Special method __init__ is to created to getting a value:
    def __init__(self, cpu, ram):   # passing arguments(value given by the user)
        # instance variable
        self.cpu = cpu
        self.ram = ram

    # create a method/function
    def Lap_config(self):
        print("Laptop configuration,", self.cpu, self.ram, self.battery)

    # creating an own methods to compare the ram of the laptop
    def compare(self, other):       # self is denotes the call object, other denotes the comparing one

        # write an if statement to check the value with a condition
        if self.ram > other.ram:
            print("Intel laptop gets higher ram in my case")
        elif self.ram == other.ram:
            print("Both of them has similar amount of ram")
        else:
            print("Ryzen laptop gets higher ram in my case")


# creating an object obj1 for the computer class, also create many object for the class if you want
lap1 = Laptop("i7", 16)             # () is a constructor in this place
lap2 = Laptop("Ryzen 7", 16)        # passing value to arguments

# After creating an object, we need to call the object for printing those stuffs
lap1.Lap_config()
lap2.Lap_config()

# comparing the two laptop configuration of the ram which one gets higher
lap1.compare(lap2)

