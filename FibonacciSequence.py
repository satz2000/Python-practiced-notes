# Creating a Fibonacci series

# Getting input from the user ad
n = int(input("Enter a number: "))

# fibonacci function
def fibonacci(n):
    # starting value will be 0 and 1. Adding next 2 values is the method for finding fib series number
    x = 0
    y = 1
    # user input is 1
    if n == 1:
        print(x)

    # user input value is greater than 1
    else:
        print(x)       # printing 1st number that are stored in x
        print(y)       # printing 2nd number that are stored in y

        # using for loop to looping through the end number is excluded
        for i in range(2, n):
            # adding two values
            op = x + y
            # swapping the value for adding the next two values that are stored in op
            x = y
            y = op
            # op value is greater than 100, breaks the loop
            if op > 100:
                break
            # print lesser than 100 values only
            print(op)

# call the function
fibonacci(n)
