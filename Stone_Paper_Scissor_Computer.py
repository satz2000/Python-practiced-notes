# getting the user's name as input
import random

user = input("Enter ur name: ")
print("----------------------------------------------------------------")

# Some comments for the user understanding
print("Rule of this game:")
print("There will be a 3 rounds, \nUser wins more than 1 rounds will be Final Winner of this Game")
print("List of choice, pick anyone given below:\n1. stone\n2. paper\n3. scissor")
print("----------------------------------------------------------------")

a = 1
round = 3
user_wc = 0
comp_wc = 0
while a <= round:
    print(f"Round No: {a}")
    user_choice = input(f"{user}, ur choice? ").lower()
    computer = random.choice(["stone", "paper", "scissor"])
    print(f"Bot choice is, {computer}")

    if user_choice == computer:
        print(f"Round No: {a}, Tie")

    elif user_choice == "stone":
        if computer == "paper":
            print(f"Round No {a}, Bot wins")
            comp_wc += 1
        else:
            print(f"Round No {a}, {user} wins")
            user_wc += 1

    elif user == "paper":
        if computer == "scissor":
            print(f"Round No {a}, Bot wins")
            comp_wc += 1

        else:
            print(f"Round No {a}, {user} wins")
            user_wc += 1

    elif user == "scissor":
        if computer == "stone":
            print(f"Round No {a}, Bot wins")
            comp_wc += 1
        else:
            print(f"Round No {a}, {user} wins")
            user_wc += 1

    else:
        print(f"Invalid input from {user}")

    print("----------------------------------------------------------------")
    a += 1

if user_wc > comp_wc:
    print(f"CONGRATS......, \n{user.capitalize()} Won This Game by {user_wc}:{comp_wc}")
elif comp_wc > user_wc:
    print(f"OOPS......, \n Bot Won This Game by {comp_wc}:{user_wc}")
else:
    print("Game is TIE")
