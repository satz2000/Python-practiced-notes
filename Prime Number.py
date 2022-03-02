# To find given number is prime number or not
num = int(input("Enter a number: "))

# using for loop to find it
for i in range(2, num):
    if num % i == 0:                    # condition statements
        print("Not Prime number")
        break                           # if condition is true break the loop

# if condition is false, then print else condition
else:
    print("Prime number")
