"""
creating an empty array to store value from user input and print it,
then getting user input for searching the elements that are present in it
if its present print the index value of that number, if its not mean just print else part
"""

# import the array packages
from array import *

# create an empty array for storing the user input values in it
arr = array("i", [])

# getting the input value from user for the length of array
n = int(input("Enter a length of array: "))

# using for loop to getting input from user and store a value in array
for i in range(n):
    # getting n number value from the user based on length of array given by user
    user = int(input("Enter a value: "))
    # append the value into the empty array
    arr.append(user)

print(arr)

# user enter a value to search a value in that array, if its present print the index value of that elements
search_element = int(input("Enter a value to search: "))

# using range function to get the index value of the elements is stored in an array
for e in range(len(arr)):

    # if the search elements is equal to the elements in array
    if search_element == arr[e]:
        # print the index number of that value and break the loop
        print(f"Value {search_element} is present at Index of {e}")
        break

# if user enter an elements that's not present in the array, then print this statement
else:
    print(f"{search_element}, Not present in the array")


print("----------------------------------------------------------------------------------------------")
### Find maximum from the array without using inbuilt functions
arr = [12, 5, 44, 2, 43]
max_val = arr[0]
for x in arr:
    if x > max_val:
        max_val = x
print(max_val)


print("----------------------------------------------------------------------------------------------")
### Adding two array using for loop
arr1 = array("i", [12, 5, 44, 2, 43])
arr2 = array("i", [11, 32, 43, 5, 6])
# creating an empty array to append the value
arr = array("i", [])

# increment the index value
index = 0
for i in arr1:
    # adding the 1st value from the arr1(using loop) and arr2(using index number to add each number)
    val = i + arr2[index]
    arr.append(val)
    index += 1
print(arr)

# if ur value are stored in array format using this simple adding method
arr3 = arr1 + arr2
print(arr3)