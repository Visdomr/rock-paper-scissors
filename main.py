import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

print("Welcome to Rock, Paper, Scissors!")
player_choice = input(
    "Please make your choice. Enter 0 for Rock, 1 for Paper, 2 for Scissors: ")
computer_choice = random.randint(a:0, b:2)
print(f"Computer chose: {computer_choice}")
