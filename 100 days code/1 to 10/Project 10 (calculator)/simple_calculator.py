from operations import operators
from art import logo
from os import system
from sys import exit

def calculator():
    """This funtion takes inputs and calculates various arithmatic operations"""

    print(logo)
    first_num = float(input("What's the first number?: "))
    for symbol in operators:
        print(symbol)

    should_continue = True
    while should_continue:
        oper = input("Pick an operation: ").strip()
        second_num = float(input("What's the next number?: "))
        func = operators[oper]
        result = func(first_num, second_num)
        print(f"{first_num} {oper} {second_num} = {result}")

        restart = input(f"\nType 'y' to continue calculating with {result} or\nType 'n' to start a new calculaton or\nType exit to EXIT \n").lower()
        if restart == 'y':
            first_num = result
        elif restart == 'n':
            should_continue = False
            system('cls')
            calculator()
        else:
            exit()

calculator()