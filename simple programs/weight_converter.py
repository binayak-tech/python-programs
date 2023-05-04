weight = float(input("Enter your weight: "))
measure = input("Enter (L)bs or (K)g: ")
if measure.upper() == "L":
    weight /= 2.205
    print(f"You are {weight} kg")
elif measure.upper() == "K":
    weight *= 2.205
    print(f"You are {weight} pounds") 
else:
    print("Give correct units")

