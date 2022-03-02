"""
# Why we use for else condition ?
# For checking the specific number or checking the condition is true
# if the condition is false we just print single line in else condition.
"""

# To check whether the given number is divisible by 5 then print the number
# if it's not then print "Given is not divisible by 5"
nums = [34, 53, 32, 20, 39]

for num in nums:
    if num % 5 == 0:
        print(num)
        break           # If condition is True it's break the loop

# print else part, after the condition is false
else:
    print("Given number is not divisible by 5")
