"""
# What is recursion?
    Recursion is calling its self, without using any loop
"""

# import sys packages for get and set the recursion limit
import sys
print("Default limit range is",sys.getrecursionlimit())

# set the recursion limit upto 1500
sys.setrecursionlimit(1500)
print("Set limit range upto", sys.getrecursionlimit())

# incrementing value
i = 1
# creating function
def greeting():
    # using the global variable in function
    global i

    # printing the value with increment number
    print("Hello", i)

    # incrementing
    i += 1

    # calling inside a function means calling by itself
    #greeting()

# again calling the function for printing the value
greeting()



print("--------------------------------------------------------------------------------------")


# Factorial using recursion method
print("Factorial using recursion method:")

n = int(input("Enter a number: "))
def fact(n):
    # factorial of 0 is 1 then factorial of 1 is 1
    x = 1
    if n == 1:
        return x
    else:
        return n * fact(n-1)

print(fact(n))