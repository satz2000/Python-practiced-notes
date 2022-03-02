# Here we see about different types of methods in class
"""
class has three types of methods:
        * Instance methods(to create a methods for getting and setting the value)
            * Accessor method (to get the value)
            * Mutator method (to set/change the value)
        * static methods(to create a methods for using class variable)
        * class methods(to create a class for doing extra things not using any values in it)T
"""

# creating class using the keyword class and gives a name to that class
class Methods:

    # creating a class variable
    global_variable = "Hello World"

    # creating a special methods called __init__ or constructor
    def __init__(self):
        self.val1 = "variable 1"        # Instance variable
        self.val2 = "variable 2"        # Instance variable
        self.val3 = "variable 3"        # Instance variable

    # Instance methods:
    def get_value(self):                # Accessor method
        print(self.global_variable, self.val1, self.val2, self.val3)

    def set_val1(self, value):         # mutator method
        self.val1 = value

    # class methods:
    @classmethod
    def update_class_variable(cls, value):
        cls.global_variable = value

    # static methods:
    @staticmethod
    def info():
        print("just used for printing the information/ extra stuff")

# creating an object for the class
obj1 = Methods()                        # () is constructor
obj2 = Methods()                        # creating 2nd object

# update/ set a value for val1 variable
obj1.set_val1("value 10")

# updating the class variable by creating a class-methods
obj1.update_class_variable("Hello G!")

# call the methods using obj1 to print the value
obj1.get_value()
obj2.get_value()

