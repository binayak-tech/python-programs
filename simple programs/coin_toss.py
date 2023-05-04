#importing random module to generate random integers
from random import randint

print("\n-----COIN TOSS-----\n")
a = 1

while a == 1:
# Loop set for invalid inputs
    
    # taking values and checking against the expected values
    value = input("(Heads/Tails) Your Call: ").lower()
    print("")
    if value in ['heads', 'tails']:
        #random integer is taken into toss variable 
        toss = randint(2, 100)

        #even number means heads and odd means tails
        if value == "heads" and toss % 2 == 0:
            print("Heads \n You Won!\n")
        elif value == "tails" and toss %2 != 0:
            print("Tails \n You Won!\n")
        else:
            val ="Heads"
            if toss %2 != 0: val = "Tails" 
            print(f"You Lost, Its {val} \n")
        a = 2
    else:
        print("Invalid Input! \n Try again \n")