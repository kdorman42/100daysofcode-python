
import os

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "cash": 0
}


def clear_console():
    """Clears the console"""
    command = 'clear'
    if os.name in ['nt', 'dos']:  # If Machine is running on Windows, use cls[
        command = 'cls'
    os.system(command)


def print_report():
    """Prints a report with resources and cash amount."""
    print(
        f"\nWater: {resources['water']}mL"
        f"\nMilk: {resources['milk']}mL"
        f"\nCoffee: {resources['coffee']mL}"
        f"\nCash: {resources['cash']:.2f}"
    )


def check_resources(drink):
    """Checks if there are enough resources to make the drink. Returns True
    if resources are sufficient and False if insufficient."""
    if MENU[drink]["ingredients"]["water"] > resources["water"]:
        print("Sorry, there is not enough water.")
        make_order = False
    elif MENU[drink]["ingredients"]["milk"] > resources["milk"]:
        print("Sorry, there is not enough milk.")
        make_order = False
    elif MENU[drink]["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry, there is not enough coffee.")
        make_order = False
    else:
        make_order = True
    return make_order


def take_money():
    """Prompts the user to enter their cash and calculates the total."""
    quarters = int(input("Quarters:  "))
    dimes = int(input("Dimes:  "))
    nickels = int(input("Nickels:  "))
    pennies = int(input("Pennies:  "))
    total_cash = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
    return total_cash


def process_money(cash_given, drink):
    """Takes the cash input by user, checks that it's enough, and returns
    True if sufficient and False if not."""
    item_cost = MENU[drink]["cost"]
    if cash_given < item_cost:
        print("Sorry, that's not enough money. Money refunded.")
        make_order = False
    elif cash_given > item_cost:
        print(f"Here is ${(cash_given - item_cost):.2f} dollars in change.")
        make_order = True
    else:
        resources["cash"] += cash_given
        make_order = True
    return make_order


def make_drink(drink):
    """Deducts resources from resource counts and delivers drink."""
    resources["water"] -= MENU[drink]["ingredients"]["water"]
    resources["milk"] -= MENU[drink]["ingredients"]["milk"]
    resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
    print(f"Here is your {drink}. ☕ Enjoy!")


def coffee_program():
    """Takes user's order, checks for enough resources,
    takes cash, makes change, and delivers drink."""
    order = input("What would you like? (espresso/latte/cappuccino):  ").lower()

    while order not in ['report', 'off', 'espresso', 'latte', 'cappuccino']:
        print("Invalid input.")
        clear_console()
        return True
    if order == "report":
        print_report()
        clear_console()
        return True
    elif order == "off":
        return False
    else:
        proceed = check_resources(order)
        if not proceed:
            clear_console()
            return True
        print(f"The cost is {MENU[order]['cost']}. Please insert coins.")
        accept_cash = take_money()
        cash_accepted = process_money(accept_cash, order)
        if not cash_accepted:
            clear_console()
            return True
        make_drink(order)
        return True

# Set machine on by default
make_coffee = True

# If machined is turned off, make_coffee is set to False and program stops.
while make_coffee:
    make_coffee = coffee_program()


