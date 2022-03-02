# Build a candy machine

avl = 50
# To show the available candies for the user
print(f"Available candy are {avl}")
user = int(input("How any candy you want? "))

# to create an increment variable for while loop
a = 1

while a <= avl:
    # user enter a value greater than available stocks, then break entire loop
    if user > avl:
        # show the message to the user
        print("Sorry... Out of stock!")
        break

    else:
        # if user enter a value lesser than available, print the candy
        print(f"Candy {a}")
        # from this condition, it prints overall candy, but we want user entered amount candy only
        if user == a:
            break
        a += 1          # increment the value of a by 1 for each iteration

# finally, print quotes to the customer
print("Have a nice day!")
