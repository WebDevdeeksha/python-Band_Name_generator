from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:
    options = menu.get_items()

    choice = input(f"\nThere are the options: {options}\nAND YES IF YOU DON'T WANT ANYTHING YOU ARE FREE TO SAY 'OFF' TO TURN THE COFFEMAKER OFF OR REPORT TO CHECK THE LEFT AMOUNT\nWhat is your choice? ").lower()
    if (choice == "off"):
        is_on = False
        print("It's turning off!")
    elif (choice == "report"):
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        # print(f"\nThe cost of your drink is💲{drink.cost}")

        if (coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost)):
            coffee_maker.make_coffee(drink)


   
        
        

        


