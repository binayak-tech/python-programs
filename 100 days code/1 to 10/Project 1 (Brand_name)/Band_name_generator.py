print("\t------BAND NAME GENERATOR------", end = "\n")
username = input("What is your first name?\n")
pet = input("Do you have/had a pet? (y/n) - ")

# This two blocks will combine both pet name and username and suggest a band name
if pet.upper() == 'Y':
    pet_name = input("What is your pet's name?\n")
    print("Your Band name can be "+username+" "+pet_name)
else:
    word = input("Describe your band in one word\n")
    print("Your Band name can be "+username+" "+word)