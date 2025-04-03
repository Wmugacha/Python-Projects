#Rock, Paper & Scissors Games
import random

game = ("rock","paper","scissors")
is_running = True

while is_running:
    computer = random.choice(game)
    player = None

    while player not in game:
        player = input("What is your pick? [rock, paper or scissors?]: ")
    
    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It is a TIE!!")
    elif player == "rock" and computer == "sciccors":
        print("You WIN!!")
    elif player == "paper" and computer == "rock":
        print("You WIN")
    elif player == "scissors" and computer == "paper":
        print("You WIN")
    else:
        print("You LOSE")

    if not input("Do you want to play again? (y or n?): ") == "y":
        is_running = False

print("Thanks for Playing!!")