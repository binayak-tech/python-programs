from art import logo
from os import system

def highest_bidder(bids):
    highest_bid = 0
    winner = ""
    for name in bids:
        if bids[name] > highest_bid:
            highest_bid = bids[name]
            winner = name
    print(f"The winner is {winner} with a highest bid of ₹{highest_bid}.")

 
print("Welcome to the decret auction program.")
repeat = True
auction_bids = {} 
while repeat == True:
    print(logo)
    name = input("What is your name?: ")
    bid_amount = int(input("What's your bid?: ₹"))

    auction_bids[name] = bid_amount




    go = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if go == 'no':
        repeat = False
        system('cls')
        highest_bidder(auction_bids)
    else:
        system('cls')
