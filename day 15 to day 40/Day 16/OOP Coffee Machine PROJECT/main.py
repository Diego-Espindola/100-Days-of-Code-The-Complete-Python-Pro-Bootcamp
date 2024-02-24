from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
menu = Menu()
coffee_machine = CoffeeMaker()
money = MoneyMachine()
while is_on:
    choice = input(f"What would you like? ({menu.get_items()}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_machine.report()
        money.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_machine.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)
