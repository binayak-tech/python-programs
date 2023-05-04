from art import vs, logo
from game_data import data
from random import choice
from os import system
from sys import exit

########################


def pick():
    """It gives a random person's_data"""
    return choice(data)


def format_data_item(data_item):
    """This function formats the data and
    saves each value of keys into variables"""

    name = data_item['name']
    description = data_item['description']
    country = data_item['country']
    return f"{name}, a {description}, from {country}."


def compare(data_a, data_b):
    """This functions compares the followers
    of two account, and returns 'A' or 'B' depending on 
    who has more followers"""
    if data_a > data_b:
        return "A"
    else:
        return "B"


def main():
    print(logo)
    account_a = pick()
    account_b = pick()
    score = 0
    should_continue = True
    while should_continue:

        while account_a == account_b:
            account_b = pick()
        
        followers_a = account_a['follower_count']
        followers_b = account_b['follower_count']

        print(f"Compare A: {format_data_item(account_a)}")
        print(vs)
        print(f"Against B: {format_data_item(account_b)}")
        format_data_item(account_b)

        user_choice = input("Who has more followers? Type 'A' or 'B': ").strip().upper()
        result = compare(followers_a,followers_b)
        
        if user_choice == result:
            system('cls')
            print(logo)
            score +=1
            print(f"\nYou're right! Current score: {score}")
            account_a = account_b
            account_b = pick()
            should_continue = True
        else:
            system('cls')
            should_continue = False
            print(f"You're wrong! Current score: {score} \n Game Over!") 


main()