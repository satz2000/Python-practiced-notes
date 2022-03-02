"""
1. Break            # Breaks the statement if the condition is True
2. Continue         # Continue to the next line if the condition is True
3. Pass             # Just skip the execution block
"""

# Break condition
for i in range(1, 26):
    print(i)
    if i == 15:
        break


# Continue
for i in range(1, 51):
    if i % 3 == 0:
        continue
    print(i)

# Pass
for i in range(1, 11):
    if i % 2 == 0:
        pass
    else:
        print(i)
