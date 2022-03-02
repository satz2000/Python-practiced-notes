# Find the factorial value

# getting input value from the user
n = int(input("Enter a number: "))

# create a function for finding factorial for the given number
def fact(n):
    # initialize the value x = 1, factorial of 1 is 1
    x = 1

    # if user enter the input value is 1, then print value of 1 factorial
    if n == 1:
        print(x)

    # if input greater than 1
    else:
        for i in range(2, n+1):         # we know factorial of 1 is 1, so start with 2 in range function
            # multiplying the value with each other, and values are stored in that by default value is 1
            x = x * i
        print(x)

fact(n)

