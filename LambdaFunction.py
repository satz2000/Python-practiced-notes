"""
# What is lambda function ?
    Lambda function is an Anonymous function, it uses only one expression.
"""

# creating a function
def square(a):
    return a*a

print(square(5))
# instant of creating function for single expression and also not reusable code that time we use lambda expression
print("-------------------------------------------------------------------")


print("Squaring a number:")
# creation a lambda function for squaring a number
a = int(input('Enter a number: '))
val = lambda a: a * a           # we can use only single expression
op = val(a)
print(op)


print("Adding two number:")
# creating a lambda function for adding two number
a = int(input("Enter num1: "))
b = int(input("Enter num2: "))
sum = lambda a, b: a + b
sum = sum(a, b)
print(sum)
