# Function
# Use of function - create a function should be reusable of code, whenever we want just call the function name

# creating a simple function
def hello():
    print("Hello")
    print("How are you!")
hello()

print("------------------------------------------------\nAddition of two number:")

def addition(a, b):
    return a+b

print(addition(5, 6))

print("------------------------------------------------\nPosition Arguments:")

# Types of function arguments:

# 1. Position arguments:
def registry(name, age):
    print(name)
    print(age)

# enter values in arguments required order
registry("sathish", 21)

print("------------------------------------------------\nKeyword Arguments:")

# 2. keyword arguments:
def entry(name, roll_no):
    print(name)
    print(roll_no)

# enter values with pair of keyword for avoiding input value errors
entry(name="sathish", roll_no=29)

print("------------------------------------------------\nDefault Arguments:")

# 3. Default arguments:
# assigning default value to that parameter,if user doesn't enter value then its print the default value
def sample(name, age=18):
    print(name)
    print(age)

# if user didn't fill the age parameter then it prints the default value (or) overwrite the value
sample("sathish")

print("------------------------------------------------\nVariable Length Arguments:")

# 4. Variable length arguments:
# using *b to store rest of values in b
def sum(a, *b):
    c = a
    for i in b:
        c = c + i
    print(c)

# enter multiple value to adding those values without any error or modification in code using this methods
sum(5, 5, 6, 7, 8, 9)

print("------------------------------------------------\nKeyword Variable Length Arguments:")

# 5. Keyword variable length arguments:
# using **b to store multiple value with also print keywords as well
def register(name, **data):
    c = name
    print(c)
    for x, y in data.items():
        print(f"{x} : {y}")

register(name="sathish", age=21, roll_no=29)
