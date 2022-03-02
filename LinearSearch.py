"""
# What is linear search?
    Linear search is a method of finding an element within the list. It's a sequential searching method
    Searching the element from left to right
"""

# creating a list that contains random number
ListOfNumber = [12, 3, 45, 6, 78, 34, 21, 9, 11]

# Getting integer input from the user that are present in the list or not, Find it
n = int(input("Enter a number to search in this List: "))

# Linear search using While loop
# creating a function
def LinearSearch():
    i = 0
    while i < len(ListOfNumber):

        if ListOfNumber[i] == n:
            print(f"Found at Index of {i} and Position at {i+1}")
            break
        i += 1

    else:
        print("Not Found")


LinearSearch()




# Linear search using For loop
def LinearSearch():

    i = 0

    for num in ListOfNumber:

        if n == num:
            print(f"Found at Index of {i} and Position at {i + 1}")
            break
        i += 1

    else:
        print("Not Found")

LinearSearch()
