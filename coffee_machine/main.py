import data
import os
import time

res = data.resources
espresso = data.MENU["espresso"]
latte = data.MENU["latte"]
cappuccino = data.MENU["cappuccino"]
money = 0
cont = False


def report(f_wat, f_mil, f_cof, f_mo, display):
    global res, money

    if not display:
        res['water'] -= f_wat
        res['milk'] -= f_mil
        res['coffee'] -= f_cof
        money += f_mo
    else:
        print(f"Water:{res['water']}\n Milk:{res['milk']}\n Coffee:{res['coffee']}\n Money:{money}")


def enough(wat, mil, cof, sel):
    if sel == "capuccino":
        if wat >= cappuccino['ingredients']['water'] and mil >= cappuccino['ingredients']['milk'] and cof >= \
                cappuccino['ingredients']['coffee']:
            return True
        else:
            return False
    elif sel == "latte":
        if (wat >= latte['ingredients']['water'] and mil >= latte['ingredients']['milk'] and
                cof >= latte['ingredients']['coffee']):
            return True
        else:
            return False
    else:
        if wat >= espresso['ingredients']['water'] and cof >= espresso['ingredients']['coffee']:
            return True
        else:
            return False


def dispense(amount, selected):
    if selected == 'latte':
        selected = latte
    elif selected == 'espresso':
        selected = espresso
    else:
        selected = cappuccino

    change = amount - (selected['cost'])
    if change >= 0:
        print(f"Here is {change}$ in change")
        print(f"Here is your {selection}, enjoy!")
        report(selected['ingredients']['water'], selected['ingredients']['milk'], selected['ingredients']['coffee'],
               selected['cost'], display=False)
    else:
        print("Please enter sufficient amount")


while True:
    os.system("cls")
    selection = input("What would you like? (espresso/latte/cappuccino):- ").lower()
    if selection == 'off':
        break

    elif selection == 'report':
        view = True
        report(res['water'], res['milk'], res['coffee'], money, view)
        time.sleep(5)
        continue
    elif selection == 'espresso' or selection == 'latte' or selection == 'capuccino':
        cont = enough(res['water'], res['milk'], res['coffee'], selection)
    else:
        print("Please enter a valid option")
        time.sleep(3)
        continue

    if cont:
        print("Please enter the coins")
        quart = int(input("How many quarters:- "))
        dime = int(input("How many dimes:- "))
        nickels = int(input("How many nickels:- "))
        pennies = int(input("How may pennies:- "))

        amount = quart / 4 + dime / 10 + nickels / 20 + pennies / 100
        dispense(amount, selection)
        time.sleep(5)

    else:
        print("Sorry not enough resources for the selection")
        time.sleep(3)

