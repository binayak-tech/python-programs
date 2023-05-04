car = False
while 1:
    user_command = input("> ").lower()
    if user_command == "help":
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to exit")
    elif user_command == "start":
        if car == True:
            print("Car is already started.")            
        else:
            print("Car Started -----🚓" )
            car = True
    elif user_command == "stop":
        if car == False:
            print("Car is already stopped")
        else:
            print("Car Stopped -----🔴" )
            car = False
    elif user_command == "quit":
        exit(0)
    else :
        print("I don't understand that 😕")
