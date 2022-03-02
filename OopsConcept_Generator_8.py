"""
# What is Generator?
    Generator is a simple way of creating Iterator using the keyword Yield to print the value instead of using return function.
"""


def TopTen():
    # Yield is a keyword for generator to print the value, it's not a function like a return
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

func = TopTen()

# You can also print one word by using __next__ method
print(func.__next__())

# You can also use for loop to print all value one by one
for val in func:
    print(val)