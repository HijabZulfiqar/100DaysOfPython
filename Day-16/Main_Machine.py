from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
money_machine = MoneyMachine()
coffee = CoffeeMaker()
menu = Menu()

while is_on:
    options = menu.get_items()
    choice = input(f"what would you like {options}?")
    if choice == "off":
        is_on = False
    elif choice == "report":
        money_machine.report()
        coffee.report()
    else:
        drink = menu.find_drink(choice)
        if coffee.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee.make_coffee(drink)
