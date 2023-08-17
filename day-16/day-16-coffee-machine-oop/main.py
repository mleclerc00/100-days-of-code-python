from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    order = input(f"What would you like? {options}: ")
    if order in options:
        drink = menu.find_drink(order)
        if coffee_machine.is_resource_sufficient(drink) and money_machine.make_payment(
            drink.cost
        ):
            coffee_machine.make_coffee(drink)
    if order == "report":
        coffee_machine.report()
        money_machine.report()
    if order == "off":
        is_on = False
