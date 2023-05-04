from random import choice
from art import logo
import fun
from os import system

############### Our Blackjack House Rules #####################

# The deck is unlimited in size. 
# There are no jokers. 
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.

############### Our Blackjack House Program #####################

def check(player, computer):
    """This adds the cards and checks for blackjack """

    player_value = sum(player)
    computer_value = sum(computer)

    if 11 in player and player_value > 21:
            player.remove(11)
            player.append(1)
            player_value = sum(player)
    
    if computer_value == 21 or (player_value == 21 and len(player)==2):
        final_hand(player,computer)
        main()
    
    if player_value > 21:
        print(f"\nYour final hand {player}, Final Value = {player_value}")
        print(f"Computer's final hand {computer}, Final Value = {computer_value}")
        print("You went over! You lose. 😤")
        main()
    
    else:
        print(f"Your cards {player}, Total = {player_value}")
        print(f"Computers first card: {computer[0]}")
    
        

def final_hand(player,computer):
    """This give's the final result of the game"""

    valuep = sum(player)
    valuec = sum(computer)
    print(f"\nYour final hand {player}, Final Value = {valuep}")
    while valuec < 17:
        computer.append(choice(fun.cards))
        valuec = sum(computer)
    print(f"Computer's final hand {computer}, Final Value = {valuec}")
    if valuec > 21:
        if valuep == 21:
            print("\nYou win with a BlackJack. 😎")
        else: print("\nComputer went over! You win. 😃")
    else:
        if valuec > valuep:
            print("\nYou lose. 😤")
        elif valuec == valuep:
            print("\n\Game draw. 🙃")
        elif valuep == 21:
            print("\nYou win with a BlackJack. 😎")
        else:
            print("\nYou win 😃")

def blackJack():
    print(logo)
    player = fun.player_f_draw()
    computer = fun.comp_f_draw()
    check(player,computer)
    while input("\nType 'y' to get another card, type 'n' to pass: ").strip().lower() == 'y':
        player.append(choice(fun.cards))
        check(player,computer)
    else:
        final_hand(player,computer)

def main():  
    while (input("\nDo you want to play a game of BlackJack? Type 'y' for yes and 'n' for exit: ")).strip().lower() == "y":
        system('cls')
        blackJack()
    else:
        exit()
main()