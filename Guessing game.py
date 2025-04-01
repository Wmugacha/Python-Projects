#Python Number Guessing Game
import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

while is_running:
    print("-----------Python Guessing Game------------")
    guess = input(f"Please input a number between {lowest_num} and {highest_num}: ")
    
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
    
        if guess < lowest_num or guess > highest_num:
            print("Number is out of range")
        elif guess > answer:
            print("Too high!! Try again")
        elif guess < answer:
            print("Too Low!! Try again")
        else:
            print(f"CORRECT!! The answer was {answer}")
            print(f"You answered in {guesses} guesses")
            is_running = False
    else:
        print("Invalid Guess")
        print(f"Enter a number between {lowest_num} and {highest_num}")