import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

print("Enter Q at any time to exit.")

while True:
    user_input = input("Rock, Paper, Scissors bot; make your move: ").lower()
    if user_input == "Q":
        break

    if user_input not in ["rock", "paper", "scissors"]:
        print("Enter a valid response.")
        continue

    random_number = random.randint(0, 2)
    # rock : 0, paper: 1, scissors: 2
    computer_choice = options[random_number]
    print("Console chose", computer_choice + ".")

    if user_input == "rock" and computer_choice == "scissors":
        print("You won.")
        user_wins += 1


    elif user_input == "paper" and computer_choice == "rock":
        print("You won.")
        user_wins += 1

    elif user_input == "scissors" and computer_choice == "paper":
        print("You won.")
        user_wins += 1

    else:
        print("You lost, bitch.")


print("Bye.")
