from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


barista = CoffeeMaker()
menu = Menu()
cashier = MoneyMachine()

machine_on = True

while machine_on:
    user_order = input(f"What would you like? {menu.get_items()}:  ")
    if user_order == 'off':
        machine_on = False
    elif user_order == 'report':
        barista.report()
        cashier.report()
    else:
        proceed_with_payment = barista.is_resource_sufficient(menu.find_drink(user_order))
        if proceed_with_payment:
            print(f"That will be ${menu.find_drink(user_order).cost:.2f} please.")
            proceed_with_drink = cashier.make_payment(menu.find_drink(user_order).cost)
        else:
            proceed_with_drink = False
            print("insufficient funds")
        if proceed_with_drink:
            barista.make_coffee(menu.find_drink(user_order))



