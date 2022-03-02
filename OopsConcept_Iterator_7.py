"""
# What is Iterator in python?
    Iterator is an object, which contains the method __iter__() and __next__().

    __iter__() - Iterates the values and print only one value at a time
    __next__() - prints the next value
"""

class TopTen:

    def __init__(self):
        self.num = 1                # initiate the value from 1

    # using the pre-defined function and name writing our own code
    def __iter__(self):
        return self

    # it prints the next value, at a time prints only one value
    def __next__(self):
        # loops iteration value only lesser than 10 and print it
        if self.num <= 10:
            # creating a variable for storing the value, num = 1 is given and iterating each time
            value = self.num
            self.num += 1
            return value
        # loops iteration values greater than 10, raise exception and stop printing
        else:
            raise StopIteration

# creating an object for the class TopTen
iter_obj = TopTen()

# print the value
iter_obj.__next__()

# using for loop to print the values one by one
for val in iter_obj.__iter__():
    print(val)


