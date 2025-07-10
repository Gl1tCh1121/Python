from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import sys

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
options = menu.get_items()
def coffee_machine():
    report = input(f"What would you like? ({options}): ").lower()
    if report == "report":
        coffee_maker.report()
        money_machine.report()
    elif report == "off":
        sys.exit()
    else:
        drink = menu.find_drink(report)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
    coffee_machine()
coffee_machine()
