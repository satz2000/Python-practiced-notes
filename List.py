"""
What is list?
    List is used to store multiple items in a single variable. list is Mutable (changable)
    [] is represented by List
"""

nums = [1, 2, 4, 6, 8, 4, 3, 5]
names = ['sathish', 'saran', 'raju', 'ramu']

# We see some method in list

nums.append(32)     # adding a value in the list at the end
print(nums)

nums.sort()         # sorting the list in ascending order
print(nums)

nums.pop(-1)        # remove elements from the list based on index number
print(nums)

nums.pop()          # remove the last elements from the list
print(nums)

nums.copy()         # copying the entire list
print(nums)

nums.insert(2, 10)  # insert value in 2nd index  of  the list
print(nums)

nums.remove(5)      # remove the specific elements
print(nums)

nums.reverse()      # sorting the list in descending order
print(nums)

nums.index(6)       # finding the index value of that elements
print(nums.index(6))

nums.count(4)       # count the value if how many times it present in the list
print(nums.count(4))

nums.extend(names)  # extends the list with a value or another list
print(nums)

nums.clear()        # clear the entire elements in the list
print(nums)


# Finding maximum value from the list
max(nums)

# Finding minimum value from the list
min(nums)

# Deleting multiple elements
del nums[4:]

# Sum of the entire list
sum(nums)
