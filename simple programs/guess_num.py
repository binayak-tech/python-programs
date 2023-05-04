import random
secretNumber = random.randint(0,9)
guessLimit = 3
i = 0
while i < guessLimit:
    guess = int(input('Guess The Number Between 0 to 9: '))
    if guess == secretNumber:
        print("You Won!!! \nCongratulations  👏👏" )
        break
    elif guess > 9 or guess < 0:
        print("Choose Between 0 to 9")
    else:
        print("Try Again")
    i+=1 
print("Better Luck Next Time")