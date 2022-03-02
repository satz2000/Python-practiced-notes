# Here we see about the types of variables in class
"""
class has two types of variable:
        * Class variable (creating a variable under the class name)
        * Instance variable (creating a variable inside the methods)
"""

# creating a class using keyword class and mention the name of that class
class Variables:

    # Class variable
    global_variable = 10

    # creating a special methods called __init__:
    def __init__(self, val1, val2, val3):         # this special methods are used to getting value from the user or pre-defined value
        self.val1 = val1            # these are the instance variable
        self.val2 = val2            # these are the instance variable
        self.val3 = val3            # these are the instance variable

    # Instance methods
    def get_value(self):            # Accessor methods
        return self.val1, self.val2, self.val3, self.global_variable

# creating an object for the class(if you want, you can also create multiple object)
var = Variables(12, 23, 34)         # passing value to the class

# call the methods inside the class for printing the value by using object var
print(var.get_value())