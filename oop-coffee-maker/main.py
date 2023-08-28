from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
on = True

while on:
    choice = input(f"Please place your order {menu.get_items()}:- ").lower()
    if choice == "off":
        on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                # drink is the obj corresponding to selected drink and it contains  a list from which we access cost
                coffee_maker.make_coffee(drink)
