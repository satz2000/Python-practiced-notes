# import packages that are we need it
import numpy as np

print("-----------------------------------------------------------------------")
print("Array Function:")
# creating an array using numpy package
arr = np.array([12, 2, 4, 5, 6], dtype=float)            # mention dtype to change types of array into our needs
print(arr.dtype)
print(arr)


print("-----------------------------------------------------------------------")
print("Linspace Function:")
# creating array using linspace by breaking the value into given value
# starting from 1 ends from 15 and equal broken into 10 parts
a = np.linspace(1, 15, 10)                                   # by default value is 50
print(a)


print("-----------------------------------------------------------------------")
print("Logspace Function:")
# logspace is similar to linspace but its break the value into unequal parts of each value
x = np.logspace(1, 15, 10)
print(x)


print("-----------------------------------------------------------------------")
print("Arange Function:")
# arange is similar to range function in for loop
# prints the value from staring to ending and also mention the steps as well
b = np.arange(0, 15, 2)
print(b)     # prints all the value or u can also use for loop to print one by one


print("-----------------------------------------------------------------------")
print("Ones Function:")
# this function prints array full of 1 value
z = np.ones(5)        # by default dtype is float
print(z)

# using matrix methods, 5x2 matrix of ones
z = np.ones([5, 2], int)
print(z)


print("-----------------------------------------------------------------------")
print("Zeros Function:")
# zeros function is similar to the ones function
y = np.zeros(5)        # by default dtype is float
print(y)

# using matrix methods, 5x2 matrix of ones
y = np.zeros([5, 2], int)
print(y)