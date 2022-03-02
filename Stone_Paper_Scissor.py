# Getting the user's name for reference
user1 = input("Enter ur name: ")
user2 = input("Enter ur name: ")
print("----------------------------------------------------------------")

# Some comments for the user understanding
print("Rule of this game:")
print("There will be a 3 rounds, \nUser wins more than 1 rounds will be Final Winner of this Game")
print("List of choice, pick anyone given below:\n1. stone\n2. paper\n3. scissor")
print("----------------------------------------------------------------")

a = 1
round = 3
user1_wc = 0
user2_wc = 0
while a <= round:
    print(f"Round no: {a}")
    user1_choice = input(f"{user1}, your choice? ").lower()
    user2_choice = input(f"{user2}, your choice? ").lower()

    if user1_choice == user2_choice:
        print(f"Round No: {a}, Tie")

    elif user1_choice == "stone":
        if user2_choice == "paper":
            print(f"Round No {a}, {user2} wins")
            user2_wc += 1
        else:
            print(f"Round No {a}, {user1} wins")
            user1_wc += 1

    elif user1_choice == "paper":
        if user2_choice == "scissor":
            print(f"Round No {a}, {user2} wins")
            user2_wc += 1

        else:
            print(f"Round No {a}, {user1} wins")
            user1_wc += 1

    elif user1_choice == "scissor":
        if user2_choice == "stone":
            print(f"Round No {a}, {user2} wins")
            user2_wc += 1

        else:
            print(f"Round No {a}, {user1} wins")
            user1_wc += 1

    else:
        print("Invalid input")

    print("----------------------------------------------------------------")
    a += 1

if user1_wc > user2_wc:
    print(f"CONGRATS......, \n{user1.capitalize()} Won This Game by {user1_wc}:{user2_wc}")
elif user2_wc > user1_wc:
    print(f"CONGRATS......, \n{user2.capitalize()} Won This Game by {user2_wc}:{user1_wc}")
else:
    print("Game is TIE")

