# Printing some patterns

# 1. printing (4 * 4) of #
print("1. Printing # in 4 times:")
for i in range(4):
    for j in range(4):
        print("# ", end="")

    print()

# 2. printing cross pattern
print("2. Printing cross pattern:")
for i in range(4):
    for j in range(i+1):
        print("# ", end="")

    print()

# 3. printing cross pattern in reverse order
print("3. printing cross pattern in reverse order")
for i in range(4):
    for j in range(4-i):
        print("# ", end="")

    print()

# Some exercise:
print("Some exercise:")
"""
# printing number in order like this:
1 2 3 4
2 3 4
3 4
4
"""

num = "1234"
for i in range(len(num)):
    print(num[i:])


"""
# printing number in order like this:
A P Q R
A B Q R
A B C R
A B C D
"""
A = "ABCD"
B = "PQR"
for i in range(4):
    print(A[:i+1] + B[i:])
