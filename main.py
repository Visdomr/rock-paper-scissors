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

game_images = [rock, paper, scissors]

print("Welcome to Rock, Paper, Scissors!")

# Score variables
player_score = 0
computer_score = 0
score_limit = 3  # Optional: Set to 0 or None for no limit

while True:
    print(f"\nScore: You {player_score} - Computer {computer_score}")
    user_input = input("Enter 0 for Rock, 1 for Paper, 2 for Scissors, or 'q' to quit: ").lower()

    # Check for quit
    if user_input in ['q', 'quit']:
        print(f"\nFinal Score: You {player_score} - Computer {computer_score}")
        if player_score > computer_score:
            print("You won the match!")
        elif computer_score > player_score:
            print("Computer won the match!")
        else:
            print("The match ended in a draw!")
        print("Thanks for playing! Goodbye!")
        break

    # Try to convert input to integer
    try:
        player_choice = int(user_input)
        if player_choice < 0 or player_choice > 2:
            print("Invalid number! Please enter 0, 1, or 2.")
            continue
    except ValueError:
        print("Invalid input! Please enter a number (0, 1, 2) or 'q' to quit.")
        continue

    # Show player's choice
    print("You chose:")
    print(game_images[player_choice])

    # Computer's choice
    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    # Determine winner and update scores
    if player_choice == computer_choice:
        print("It's a draw!")
    elif (player_choice == 0 and computer_choice == 2) or \
         (player_choice == 1 and computer_choice == 0) or \
         (player_choice == 2 and computer_choice == 1):
        print("You win!")
        player_score += 1
    else:
        print("Computer wins!")
        computer_score += 1

    # Check for score limit
    if score_limit and (player_score >= score_limit or computer_score >= score_limit):
        print(f"\nFinal Score: You {player_score} - Computer {computer_score}")
        if player_score > computer_score:
            print("You won the match!")
        else:
            print("Computer won the match!")
        play_again = input("Would you like to play another match? (y/n): ").lower()
        if play_again in ['y', 'yes']:
            player_score = 0
            computer_score = 0
            print("\nStarting a new match!")
        else:
            print("Thanks for playing! Goodbye!")
            break
