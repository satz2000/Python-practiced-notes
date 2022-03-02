# If statement is a logical condition for thinking logically

"""
# Three condition are there:
    1. If
        * Nested If
    2. Elif
        * Nested Elif
    3. Else
        * Nested Ese
From this If condition we can create another If condition is called Nested If
same as elif and else.
"""

# To find given is Odd or Even & Greater than 5 or lesser than 5
number = int(input("Enter a number: "))

if number % 2 == 0:                                     # Given number is Even
    print(f"{number} is Even number.")

    # Nested if else condition
    if number > 5:                                      # Given number is greater than 5
        print(f"{number} is greater than 5")

    elif number == 5:                                   # Given number is equal to 5
        print(f"{number} is equal to 5")

    elif number < 5:                                    # Given number is lesser than 5
        print(f"{number} is lesser than 5")

    else:                                               # If above condition is False then print else part
        print(f"{number} is Negative number")

elif number % 2 != 0:                                   # Given number is Odd
    print(f"{number} is Odd number")

    # Nested if else condition
    if number > 5:                                      # Given number is greater than 5
        print(f"{number} is greater than 5")

    elif number == 5:                                   # Given number is equal to 5
        print(f"{number} is equal to 5")

    elif number < 5:                                    # Given number is lesser than 5
        print(f"{number} is lesser than 5")

    else:                                               # If above condition is False then print else part
        print(f"{number} is Negative number")

# If above condition is False then print else part
else:
    print(f"{number} is negative number")

print("Bye!")

# Some exercise
# 1. Find given number is positive or negative
num = int(input("Enter a number: "))

if num > 0:
    print("Given number is Positive")

elif num < 0:
    print("Given number is Negative")

else:
    print("Given number is 0")

# 2. Get 3 numbers from the user and Find greater number among three
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))

if num1 > num2 and num1 > num3:
    print(f"{num1} is greater than {num2} and {num3}")

elif num2 > num1 and num2 > num3:
    print(f"{num2} is greater than {num3} and {num1}")

elif num3 > num2 and num3 > num1:
    print(f"{num3} is greater than {num1} and {num3}")

else:
    print("Invalid input!")
