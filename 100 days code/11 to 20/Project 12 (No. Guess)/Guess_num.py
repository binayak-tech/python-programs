from random import randint
from art import logo
from os import system

request = False
while request == False:
    print(logo)

    number = randint(1,100)

    print("\nWelcome to the Number Guessing Game!")
    print("I have a number between 1-100 in mind.")
    difficutly = input("Choose a difficulty. Type 'easy', 'medium' or 'hard': ").strip().lower()

    if difficutly == 'easy':
        attempts = 10
    elif difficutly == 'medium':
        attempts = 7
    else:
        if difficutly != 'hard':
            print("You provided a wrong input! Difficulty is set to hard")
        attempts = 5

    for _ in range (0, attempts):
        print(f"\nYou have {attempts} attempts remaining to guess the number.")
        user_guessed = int(input("Make a guess: ").strip())

        if user_guessed < number:
            print("Too low.")
        elif user_guessed > number: 
            print("Too high")
        else:
            print(f"You got it! I had {number} in mind.")
            break
        if _ != attempts-1:
            print("Guess again.")
        else:
            print("You lose.")
    restart = input("\nType 'y' to play again, 'n' to exit: ").strip().lower()
    if restart == 'y':
        system('cls')
    else:
        request = True
