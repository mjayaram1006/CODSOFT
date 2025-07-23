import random

# Options for the game
choices = ["rock", "paper", "scissors"]

# Get user input
user = input("Choose rock, paper, or scissors: ").lower()
computer = random.choice(choices)

# Show choices
print(f"You chose: {user}")
print(f"Computer chose: {computer}")

# Determine the winner
if user == computer:
    print("It's a tie!")
elif (user == "rock" and computer == "scissors") or \
     (user == "scissors" and computer == "paper") or \
     (user == "paper" and computer == "rock"):
    print("You win!")
else:
    print("You lose!")
