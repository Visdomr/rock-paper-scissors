import random

options = ["rock", "paper", "scissors"]
my_choice = input("Choose Rock, Paper, or scissors to start: ")
computer_choice = random.choice(options)
print("You picked: ", my_choice)
print("Computer picked: ", computer_choice)

if my_choice == computer_choice:
    print("It's a tie!")
elif my_choice == "rock" and computer_choice == "scissors":
    print("You win!")
elif my_choice == "paper" and computer_choice == "rock":
    print("You win!")
elif my_choice == "scissors" and computer_choice == "paper":
    print("You win!")
else:
    print("You lose!")
