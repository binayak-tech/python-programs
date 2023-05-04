print("***Welcome to Treasure Island***\n")
print("Your mission is to find the hidden treasure")
direction = input("You are at a cross road. Which way do you wanna go 'left', 'right' or 'straight' \n").lower()

if direction == "left":
    print("\nUpppssss!!! That is the wrong way.")
    print("YOU LOST")
elif direction == "right":
    print("\nThere is a swinging cable bridge ahead, and wind is blowing fast.")
    bridge_stage = input("Do you want to 'cross' or 'wait' \n").lower()
    
    if bridge_stage == "wait":
        print("\nUpssss! Someone else found the Treasure first.\nYOU LOST")
    elif bridge_stage == "cross":
        print("\nThere are three doors ahead \n 'RED', 'GREEN' 'BLACK'")
        print("Treasure is behind one of the three doors")
        door = input("You have only one chance! Choose carefully: ").lower() 
        if door == 'red':
            print("Wohooooo!!!!! Congratulations You Found The Treasure")
        elif door == 'green':
            print("Wrong door. \nYOU LOST")
        elif door == 'black':
            print("Wrong door. \nYOU LOST")
        else:
            print("wrong input\n PLAY AGAIN")      
    else:
        print("wrong input\n PLAY AGAIN")
elif direction == "straight":
    print("\nThere are three doors ahead \n 'RED', 'GREEN' 'BLACK'")
    print("Treasure is behind one of the three doors")
    door = input("You have only one chance! Choose carefully: ").lower() 
    if door == 'red':
        print("Wohooooo!!!!! Congratulations You Found The Treasure")
    elif door == 'green':
        print("Wrong door. \nYOU LOST")
    elif door == 'black':
        print("Wrong door. \nYOU LOST")
    else:
        print("wrong input\n PLAY AGAIN")
