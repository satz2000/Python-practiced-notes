# Copying of array
"""
# Two types of copying method:
    * shallow copy
    * deep copy
"""

# importing packages
import numpy as np

print("Adding two Array:")
# adding two array
arr1 = np.array([1, 3, 5, 7, 9])
arr2 = np.array([2, 4, 6, 8, 10])

# adding two array
arr = arr1 + arr2
print(arr)

print("--------------------------------")
print("Shallow copy:")
print("Type 1,")
# shallow copy
A = np.array([1,2,3,4,5])
B = A
print(id(A))
print(id(B))

# These methods copy value of A to B with different ID, but change values from B also changes in A
print("\nType 2,")
A = np.array([1,2,3,4,5])
B = A.view()
print(id(A))
print(id(B))

print("--------------------------------")
# These methods copy value of A to B with different ID, change values from B but not affects in A
print("Deep copy:")
# Deep copy
A = np.array([1,2,3,4,5])
B = A.copy()
print(id(A))
print(id(B))