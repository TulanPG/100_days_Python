from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
#menu_item = MenuItem()
is_on = True

#print(menu.get_items())

while is_on:
    option = menu.get_items()
    print(menu.get_items())
    choice = input(f"co chcesz? ({option}): ")
    if coffee_maker.is_resource_sufficient(menu.find_drink(choice)):
        drink = menu.find_drink(choice)

        print("Mamy w zapasie, wgraj kase: ")
        print(drink.cost)
        if money_machine.make_payment(drink):
            print("zgadza się")
            coffee_maker.make_coffee(drink)
        else:
            print("złą kasa")







    else:
        print("Brak składników wybierz co innego")







#print(coffee_maker.is_resource_sufficient(menu.find_drink()))






#money_machine.report()
#coffe_maker.report()


