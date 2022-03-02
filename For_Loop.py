"""
# What is For loop?
    For loop is used for iterating in sequence order
"""

# print names in sequence order
names = ["sathish", "saran", "shiva", "ragu"]

for x in names:
    print(x)


# print number from 1 to 10 using range function
for x in range(1, 10+1):
    print(x)


# print square root of number from 1 to 50
for x in range(1, 51):
    if x ** .5 == int(x ** .5):
        print(x)
