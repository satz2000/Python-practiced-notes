# Exception Handling topic

# Always writing the code and execute the code is done.
# at the end, If code is runs successful / getting some error
# programmer wants to mention the error to user for the understanding what mistake he/she's done

# creating a function div for divide two numbers
def div():

    # getting input of integers values from the user side is num1 and num2
    num1 = int(input("Enter a number: "))
    num2 = int(input(f"Enter a number to divide {num1}, "))

    # If you want to execute the code, just write your code in execute bock
    try:
        print(num1/num2)

    # If any error occurs in try block in execution time,
    # came to exception block and explains the error to the user
    except Exception as err:                    # Exception as err mean storing the error message in err for printing it
        print(f"Expected error is, {err}")

    # If you want to print something after the execution of code / any error,
    # then write your code in final block
    finally:
        print("Thank You!")

# call the function by using the name div()
div()
