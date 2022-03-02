# Selection sort

"""
This sorting algorithm, iterates through the array and finds the smallest number in the array and
swaps it with the first element if it is smaller than the first element.
Next, it goes on to the second element and so on until all elements are sorted
"""

nums = [5, 3, 8, 6, 7, 2]
def sort():
    # creating nested loop to make many iteration until all value are sorted
    for i in range(5):
        # minimum position value is changing for each iteration to find the min value and swap them
        min_pos = i
        # creating for loop with range of value i to the end is 6
        for j in range(i, 6):
            # number of j index value is lesser than number of minimum value
            if nums[j] < nums[min_pos]:
                min_pos = j         # update the min_pos value into j

        # swapping the two variable, min value and 1st value of the list, only if it's smaller one
        temp = nums[i]
        nums[i] = nums[min_pos]
        nums[min_pos] = temp

    # print the sorted list
    print(nums)
sort()
