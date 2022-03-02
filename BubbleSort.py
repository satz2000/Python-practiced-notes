"""
# What is bubble sort?
    sorting the list by checking 1st 2 number if 2nd number lesser than 1st number,
    then swapping the two again this process is ongoing until all the number is sorted.
"""

# creating a sort function
def sort_list(list):    # passing the list of number as an arguments

    # Using nested for loop
    for i in range(len(list)-1,  0, -1):        # start at the total count value and 0 (in this case 9, 1)

        # using the for loop as range of i value for each iteration
        for j in range(i):
            # taking two number, 1st number greater than 2nd number just swap the two number again check the another number
            if list[j] > list[j+1]:
                # swapping two using temp variable
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp

# list of number
ListOfNums = [12, 23, 43, 54, 6, 56, 31, 8, 98, 61]
# call the function by passing the value
sort_list(ListOfNums)
# print the sorted list
print(ListOfNums)