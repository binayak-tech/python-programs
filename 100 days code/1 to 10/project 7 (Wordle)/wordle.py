#importing modules from same directory
from five_letter_words import fiveLetterLword
from hangman import stages, logo
import os

chosen = fiveLetterLword()
chosen_word= []
for letter in chosen:
    chosen_word += letter
    
# print (f"WORD IS = {chosen}")
word = ['_','_','_','_','_']
missed_letters = ['#','#','#','#','#']

# looping for all seven lives
k=0
while k < 7:
    guessed = input("Guess the word : _ _ _ _ _\n").upper()
    os.system('cls')

    # checking if input size = 5 
    if len(guessed) != 5 :
        print(logo)
        print(stages[k])
        print("!!!!WARNING!!!!\nONLY FIVE LETTER WORDS ARE ACCEPTED.")
        if k == 6:
            print("You lost all lives! ")
            print("####----GAME OVER----####")
        k+=1
        continue

    # converting input string to list with individual letter as a list element
    guessed_word= []
    for letter in guessed:
        guessed_word += letter
    
    # checking all the conditions for ensuring the word or any letter in the word 
    # matches the randomly selected word.
    if not guessed_word == chosen_word:
        for j in range(5):
            if guessed_word[j] == chosen_word[j]:
                word[j] = guessed_word[j]
            else:
                if (guessed_word[j] in chosen_word) and (guessed_word[j] not in  missed_letters) :
                    missed_letters[j] = guessed_word[j]
        
        # Giving hits and showing the stages of hangman
        print(logo)
        print(stages[k])
        if k == 6:
            print("You lost all lives! ")
            print("####----GAME OVER----####")
            k+=1
            continue
        print(f"Wrong Position:   {missed_letters}\nCorrect Position: {word}")
        k+=1
    else:
        print(f"You won\nWord was: {chosen}")
        break