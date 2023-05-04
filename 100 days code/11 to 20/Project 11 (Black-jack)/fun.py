import random 

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def player_f_draw():
    """This draws two cards for player"""
    return random.sample(cards,2)

def comp_f_draw():
    """This draws two cards for computer"""
    return random.sample(cards,2)

