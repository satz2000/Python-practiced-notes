def try_except_bloc():

    try:
        num1 = int(input("Enter a 1st number: "))

        op = input("Select an operator:\n1. Addition (+)\n2. Subraction (-)\n3. Multiplication (*)\n4. Division (/)"
                   "\nChoose an operator: ")

        num2 = int(input("Enter a 2nd number: "))

    except Exception as err:
        print(err)

    def BasicCalculator():

        if op == "+":
            print(f"Your answer is {num1 + num2}")

        elif op == "-":
            print(f"Your answer is {num1 - num2}")

        elif op == "*":
            print(f"Your answer is {num1 * num2}")

        elif op == "/":
            print(f"Your answer is {num1 / num2}")

        else:
            print("Please select an valid operator")

    print("Output:")
    BasicCalculator()

try_except_bloc()