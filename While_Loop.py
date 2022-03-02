"""
# What is while loop?
    While loop runs set of statement as long as condition is True, If the condition is True the execution will be stops

    We see about:
        while loop and nested while loop
"""

# print five time my name
i = 1

# while loop with a condition
while i <= 5:
    print("Sathish")
    i += 1

# After the condition is True, execute this line
print("Bye")


###### Nested loop
i = 1

while i <= 5:                       # We can change the condition to print in reverse order
    print("Sathish ", end="")

    j = 1
    while j <= 4:
        print("Pbs ", end="")
        j += 1

    i += 1
    print()                         # After complete one execution, again checking i value



###### Some exercise

# 1. Print number from 1 to 100 and skip which is divisible by 3 and 5
i = 1

while i <= 100:

    if i % 3 and i % 5 != 0:
        print(i)
    i += 1
print("Only print the number which is not divisible by 3 and 5")

