from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# MENU ITEM
# - name: The name of the drink, e.g. “latte”.
# --- cost: (float) The price of the drink, e.g 1.5.
# - ingredients: (dictionary) The ingredients and amounts required to make the drink, e.g. {“water”: 100, “coffee”: 16}.

# MENU
# --- get_items(): Returns all names of available menu items as concatenated string, e.g. “latte/espresso/cappuccino”.
# --- find_drink(order_name): Searches menu for drink by name. Returns MenuItem object if it exists, else returns None.

# COFFEE MAKER
# --- report(): Prints a report of all resources, e.g. Water: 300ml | Milk: 200ml | Coffee: 100g.
# --- is_resource_sufficient(drink) "drink" is MenuItem. Returns True when drink can be made, False if it can't.
# --- make_coffee(order) "order" is MenuItem. Deducts the required ingredients from the resources.

# MONEY MACHINE
# --- report(): Prints the current profit, e.g. Money: $0.
# --- make_payment(cost) "cost" is MenuItem. Returns True when payment is accepted, or False if insufficient.

# Print Report ## Check resources sufficient ## Process coins ## Check transaction successful ## Make coffee.

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

in_use = True
while in_use:
    options = menu.get_items()
    choice = input(f"Which drink would you like? {options}:")
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        in_use = False
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)