# Getting input from user is important for project:

# Type 1:
"""
# Getting int from the user for adding 2 number
# Convert the input into integer for adding two number
"""

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
ans = num1 + num2
print(f"Adding the Two number is about {ans}")


# Type 2:
"""
# Just getting single character from the user
# If user enter a more than a single character our input function takes only the 1st character from the user input 
"""

char = input("Enter a character: ")[0]
print(char)


# Type 3:
"""
# Getting the input from user for evaluating the value
# For evaluating, use the eval function.
"""

val = eval(input("Enter a evaluation number: "))
print(val)
