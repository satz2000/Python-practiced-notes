"""
# What is decorator ?
    Decorator is powerful tools in python,
    creating a new function to modifying the existing function or modules,
    without touching or modifying the existing code in that previous function
"""

# In this function, no modification in the code
def div(a, b):
    return a/b

# creating another func to modify div function with touch that func
def smart_div(func):

    # creating a inner function to modify the code what you want
    def inner_func(a, b):
        # this is the condition
        if a < b:
            a, b = b, a
        return func(a, b)           # return the function of div with a parameter of a and b in inner func
    return inner_func               # Finally, return the inner function

# creating an object div and passing div function as parameter to smart_div function
div = smart_div(div)
print(div(2, 4))