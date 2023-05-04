import random

# RULES
# rock wins against scissors
# paper wins against rock
# scissors wins agains paper

#ASCII ARTS assigned to variables
rock ='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper ='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''

scissors ='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# computer choses randomly from all possible choices
game = [rock, paper, scissors]
random_sign = random.randint(0,2)

# collecting user input 
user_sign = int(input("What do you choose?\nType 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_sign not in range(0,3): 
    print("You typed an invalid number, You lose!")
else:
    print(f"{game[user_sign]}")

    print(f"\nComputer chose:\n{game[random_sign]}")

    # checking the rules for decision
    if user_sign == random_sign:
        print("Game Draw")
    elif user_sign == 0 and random_sign == 2:
        print("You Won")
    elif user_sign == 1 and random_sign == 0:
        print("You Won")
    elif user_sign == 2 and random_sign == 1:
        print("You Win")
    else:
        print("You Lose")
