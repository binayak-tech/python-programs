order = ["espresso", "latte", "cappuccino"]

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.50
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "milk": 150
        },
        "cost": 2.50
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100
        },
        "cost": 3.00
    }
}
profit = 0
resources = {
    "water": 1000,
    "coffee": 150,
    "milk": 1000
}


def sufficient_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return 0
        return 1


def insert_coins(coins_needed):
    print("Please insert coins.")
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickles?: "))
    pennies = float(input("How many pennies?: "))

    total_paid = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    if total_paid < coins_needed:
        print(f"Sorry that's not enough money. ${total_paid} refunded")
        return 0
    elif total_paid > coins_needed:
        refund = total_paid - coins_needed
        refund = "{:.2f}".format(refund)
        print(f"Here ${refund} in change")
        return 1
    else:
        return 1


is_active = True
while is_active:
    if resources["coffee"] < 18 or resources["water"] < 50:
        print("Out of order")
        is_active = False
        continue

    choice = input("What would you like? (espresso/latte/cappuccino): ").strip().lower()

    if choice == "report":
        print(f"The current resource values.")
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")

    elif choice == "off":
        is_active = False

    elif choice in order:
        drink = MENU[choice]
        products = drink["ingredients"]
        if sufficient_resources(products):
            if insert_coins(drink["cost"]):
                for product in products:
                    resources[product] -= products[product]
                profit += drink["cost"]
                print(f"Here is your {choice} ☕ enjoy")

    else:
        print("invalid Input")


# ############################ ANOTHER METHOD ############################
# water = 500
# coffee = 50
# milk = 500
# money = 0
# is_active = True
#
#
# def insert_coins(coins_needed):
#     print("Please insert coins.")
#     quarters = float(input("How many quarters?: "))
#     dimes = float(input("How many dimes?: "))
#     nickles = float(input("How many nickles?: "))
#     pennies = float(input("How many pennies?: "))
#
#     total_paid = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
#     if total_paid < coins_needed:
#         print(f"Sorry that's not enough money. ${total_paid} refunded")
#         return 0
#     elif total_paid > coins_needed:
#         refund = total_paid - coins_needed
#         refund = "{:.2f}".format(refund)
#         print(f"Here ${refund} in change")
#         return 1
#     else:
#         return 1
#
#
# while is_active:
#     if coffee < 18 or water < 50:
#         print("Out of order")
#         is_active = False
#         continue
#
#     coffee_type = input("What would you like? (espresso/latte/cappuccino): ").strip().lower()
#
#     if coffee_type == "espresso":
#         if water >= 50:
#             if coffee >= 18:
#                 if insert_coins(1.50):
#                     print(f"Here is your {coffee_type} ☕ enjoy")
#                     money += 1.50
#                     water -= 50
#                     coffee -= 18
#             else:
#                 print("Sorry not enough coffee")
#         else:
#             print("Sorry there is not enough water")
#
#     elif coffee_type == "latte":
#
#         if water >= 200:
#             if coffee >= 24:
#                 if milk >= 150:
#                     if insert_coins(2.50):
#                         print(f"Here is your {coffee_type} ☕ enjoy")
#                         money += 2.50
#                         water -= 200
#                         coffee -= 24
#                         milk -= 150
#                 else:
#                     print("Sorry Not enough milk.")
#             else:
#                 print("Sorry not enough coffee.")
#         else:
#             print("Sorry there is not enough water.")
#
#     elif coffee_type == "cappuccino":
#
#         if water >= 250:
#             if coffee >= 24:
#                 if milk >= 100:
#                     if insert_coins(3.00):
#                         print(f"Here is your {coffee_type} ☕ enjoy")
#                         money += 3.00
#                         water -= 250
#                         coffee -= 24
#                         milk -= 100
#                 else:
#                     print("Sorry Not enough milk.")
#             else:
#                 print("Sorry not enough coffee.")
#         else:
#             print("Sorry there is not enough water.")
#
#     elif coffee_type == "report":
#         print(f"The current resource values.\nWater: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")
#
#     elif coffee_type == "off":
#         is_active = False
