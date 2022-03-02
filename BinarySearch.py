"""
# What is Binary Search?
    Binary search is an algorithm that finds the position of an element in a sorted array.
    It divides a list into two halves.
    Then, A search value compares if a value is higher or lower than the middle value in the list
"""

# List of number that are not sorted in ascending order
ListOfNumber = [12, 23, 43, 54, 6, 56, 31, 8, 98, 61]
SortedList = []                 # For storing the sorted value

def SortList():
    # First we need to sort the list, then divide into two part of list
    while ListOfNumber:         # it runs to loop until all each number is used

        # storing minimum value is equal to 1st number in the list and updating it everytime for each iteration
        min_val = ListOfNumber[0]

        for num in ListOfNumber:

            # each number in this list <= 1st number of the list
            if num < min_val:
                # then store the number into min value
                min_val = num
        # then append the number into sorted list variable
        SortedList.append(min_val)
        # after updating the number, then remove from list because of next number we want search it
        ListOfNumber.remove(min_val)

SortList()

# creating variable for finding the position of the number where it's present it and stored the position in it
pos = 0

# creating a function for Binary Search
def BinarySearch():

    # Getting input from the user to search the number, where it was present
    n = int(input("Enter a search element: "))

    # We need to find the lower value and higher value, create variable for that and give starting index value
    lower_bound = 0
    upper_bound = len(SortedList) - 1

    # Lower index value is lesser than equal to upper index value, if it's greater than it then breaks the loop
    while lower_bound <= upper_bound:
        # Finding the mid-index value by adding the lower and upper index is divided by floor division of 2
        mid_bound = (lower_bound + upper_bound) // 2

        # From the sorted list, mid-index value of Sorted list value is equal to user input value (n)
        if SortedList[mid_bound] == n:
            pos = mid_bound         # then store the position value into mid-index value
            print(f"Found at {pos}")        # print the position and break the loop
            break

        # if the mid-index of sorted list not equal to user input, then comes into else part, updating the lb, ub and mb for next iteration
        else:
            # If mid-index value from the sorted list is greater than user input, then update the upper index value to -1
            if SortedList[mid_bound] > n:
                upper_bound = mid_bound - 1
            # If mid-index value from the sorted list is lesser than user input, then update the upper index value to +1
            else:
                lower_bound = mid_bound + 1

    # If number isn't present from the entire Sorted list, then print statement
    else:
        print('Not Found')

# call the function
BinarySearch()