# Swapping 2 Numbers
a = 5
b = 6

# Swapping two number with 3rd variable:
temp = a
a = b
b = temp
print(a, b)

# Swapping two number with Formula:
a = 5
b = 6

a = a + b           # a = 11, its takes 4bits (Extra 1bits are wasting here)
b = a - b           # b = 5, its takes 3bits
a = a - b           # a = 6, its takes 3bits
print(a, b)

# Swapping two number with XOR methods:
a = 5
b = 6

a = a ^ b
b = a ^ b
a = a ^ b
print(a, b)

# Swapping two numbers with Special methods in python:
a = 5
b = 6

a, b = b, a         # a ROT_TWO methods of swapping numbers
print(a, b)
