MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

resources["Money"] = 0.0


def check_ingredients(user_choice):
    requirements = MENU[user_choice]["ingredients"]
    if user_choice == "latte" or user_choice == "cappuccino":
        for x in resources:
            if requirements[x] > resources[x]:
                print(f"Sorry, there is not enough {x}.")
                return False
            else:
                return True
    else:
        if requirements["water"] > resources["water"]:
            print("Sorry, there is not enough water")
            return False
        elif requirements["coffee"] > resources["coffee"]:
            print("Sorry, there is not enough coffee")
            return False
        else:
            return True


def resource_management(user_choice):
    requirements = MENU[user_choice]["ingredients"]
    if user_choice == "latte" or user_choice == "cappuccino":
        resources["water"] -= requirements["water"]
        resources["milk"] -= requirements["milk"]
        resources["coffee"] -= requirements["coffee"]
    else:
        resources["water"] -= requirements["water"]
        resources["coffee"] -= requirements["coffee"]


def payment():
    print("Please insert coins.")
    coin1 = int(input("How many quarters?:")) * 0.25
    coin2 = int(input("How many dimes?:")) * 0.1
    coin3 = int(input("How many nickles?:")) * 0.05
    coin4 = int(input("How many pennies?:")) * 0.01
    payment = coin1 + coin2 + coin3 + coin4
    if payment < MENU[choice]["cost"]:
        print("Sorry that's not enough money. Money refunded")
    elif payment > MENU[choice]["cost"]:
        return_change = payment - MENU[choice]["cost"]
        resources["Money"] += MENU[choice]["cost"]
        print(f"Here is ${return_change} in change.\nHere is your {choice}, enjoy!")
        resource_management(choice)
    else:
        resource_management(choice)
        resources["Money"] += MENU[choice]["cost"]
        print(f"Here is your {choice}, enjoy!")
        resource_management(choice)


in_use = True
while in_use:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        in_use = False
    elif choice == "report":
        print(
            f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${resources['Money']}")
    elif choice == 'latte' or 'espresso' or 'cappuccino':
        if check_ingredients(choice):
            payment()
        else:
            print(
                f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${resources['Money']}")
