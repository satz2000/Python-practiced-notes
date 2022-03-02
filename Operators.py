"""
# What is operators?
   Operators are used to perform operations on variables and values.

# Types of operators:
1. Arithmetic operators
2. Assignment operators
3. Comparison operators
4. Logical operators
5. Identity operators
6. Membership operators
7. Bitwise operators
"""

print("1. Arithmetic operator:")
# 1. Arithmetic operator:
# Arithmetic operators are used with numeric values to perform common mathematical operations:

a = 10
b = 6

x = a + b       # Addition
print(x)
x = a - b       # Subtraction
print(x)
x = a * b       # Multiplication
print(x)
x = a / b       # Division
print(x)
x = a // b      # Floor Division
print(x)
x = a % b       # Modulus
print(x)
x = a ** b      # Exponent
print(x)

print("\n2. Assignment operator:")
# 2. Assignment operator:
# Assignment operators are used to assign values to variables:

x = 5

x += 2          # Adding itself
print(x)

x -= 1          # Sub itself
print(x)

x *= 2          # Multiply itself
print(x)

x /= 2          # Divide itself
print(x)
# remaining are not so important

print("\n3. Comparison operator:")
# 3. Comparison operator:
# Comparison operator are used to compare two values:

a = 5
b = 4

x = a > b       # checking a greater than b
print(x)

x = a < b       # checking a lesser than b
print(x)

x = a >= b       # checking a greater than or equal to b
print(x)

x = a <= b       # checking a lesser than or equal to b
print(x)

x = a == b       # checking a is equal to b
print(x)

x = a != b       # checking a is not equal to b
print(x)

print("\n4. Logical operator:")
# 4. Logical operator:
# Logical operators are used to combine conditional statements:

a = 5
b = 8

x = a > 8 and b > 5         # And operator (Checking both conditions is true)
print(x)

x = a > 5 or b > 5          # Or operator (Checking either one of the condition is true)
print(x)

x = True
x = ~x                      # Not operator (changing the value to opposite)
print(x)


print("\n5. Identity operator:")
# 5. Identity operator:
# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

x = [1, 4, 5, 3, 6, 23]
y = [1, 2, 4, 5, 8, 9]

val = x is y                # Comparing x is equal to y
print(val)

val = x is not y            # comparing x is not equal to y
print(val)


print("\n6. Membership operator:")
# 6. Membership operator:
# Membership operators are used to test if a sequence is presented in an object:

x = [1, 4, 5, 3, 6, 23]

val = 5 in x                # Checking 5 present in x
print(val)

val = 9 not in x            # Checking 9 is not present in x
print(val)
