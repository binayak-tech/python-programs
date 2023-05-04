
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

concatenated_names = ""
concatenated_names = name1 + name2
concatenated_names = concatenated_names.lower().strip()

occurance_true = 0
occurance_true += concatenated_names.count("t")
occurance_true += concatenated_names.count("r")
occurance_true += concatenated_names.count("u")
occurance_true += concatenated_names.count("e")

occurance_love = 0
occurance_love += concatenated_names.count("l")
occurance_love += concatenated_names.count("o")
occurance_love += concatenated_names.count("v")
occurance_love += concatenated_names.count("e")

score = int(str(occurance_true) + str(occurance_love))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")

elif score in range(40,51):
    print(f"Your score is {score}, you are alright together.")

else:
    print(f"Your score is {score}.")
