MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
    "water": 500,
    "milk": 400,
    "coffee": 200,
}
espresso_water = MENU["espresso"]["ingredients"]["water"]
latte_water = MENU["latte"]["ingredients"]["water"]
cappuccino_water = MENU["cappuccino"]["ingredients"]["water"]

latte_milk = MENU["latte"]["ingredients"]["milk"]
cappuccino_milk = MENU["cappuccino"]["ingredients"]["milk"]

espresso_coffee = MENU["espresso"]["ingredients"]["coffee"]
latte_coffee = MENU["latte"]["ingredients"]["coffee"]
cappuccino_coffee = MENU["cappuccino"]["ingredients"]["coffee"]

espresso_cost = MENU["espresso"]["cost"]
latte_cost = MENU["latte"]["cost"]
cappuccino_cost = MENU["cappuccino"]["cost"]





def check_ingredients(flavor):
    check = False
    if flavor == 'espresso':
        if resources["water"] >= espresso_water:
            check = True
        else:
            print("We are short of water.Sorry!🥹 ")
            check = False
        if resources["coffee"] >= espresso_coffee:
            check = True
        else:
            print("We are short of water.Sorry!🥹 ")
            check = False
    elif flavor == 'latte':
        if resources["water"] >= latte_water:
            check = True
        else:
            print("We are short of water.Sorry!🥹 ")
            check = False
        if resources["coffee"] >= latte_coffee:
            check = True
        else:
            print("We are short of coffee.Sorry!🥹 ")
            check = False
        if resources["milk"] >= latte_milk:
            check = True
        else:
            print("We are short of milk.Sorry!🥹 ")
            check = False
    elif flavor == 'cappuccino':
        if resources["water"] >= cappuccino_water:
            check = True
        else:
            print("We are short of water.Sorry!🥹 ")
            check = False
        if resources["coffee"] >= cappuccino_coffee:
            check = True
        else:
            print("We are short of coffee.Sorry!🥹 ")
            check = False
        if resources["milk"] >= cappuccino_milk:
            check = True
        else:
            print("We are short of milk.Sorry!🥹 ")
            check = False
    return check


def update_resources(flavor):
    ingredients=MENU[flavor]["ingredients"]
    for item in ingredients:
        resources[item]-=ingredients[item]
profit=0
def process_coins(flavor):

    global resources ,profit
    print("please insert coins 🤑🤑🤑 ")
    quarter = int(input("How many quarters?"))
    nickles = int(input("How many nickles?"))
    dimes = int(input("How many dimes?"))
    pennies = int(input("How many pennies?"))
    total_cost = quarter * 0.25 + nickles * 0.05 + pennies * 0.01 + dimes * 0.10
    drink_cost=MENU[flavor]["cost"]
    if drink_cost<=total_cost:

        refund=total_cost-drink_cost
        refund=round(refund,2)
        profit+=total_cost-refund
        print(f"Here is your {flavor} ☕️ Enjoy!!!")
        update_resources(flavor)
        if refund>0:
            print(f"Your change is ${refund}")
    else:
        total_cost=round(total_cost,2)
        print(f"Sorry, that's not enough money. Refunded: ${total_cost}")
def display_report():
    global resources
    print(f"water: {resources['water']}ml ")
    print(f"milk: {resources['milk']}ml ")
    print(f"coffee: {resources['coffee']}g")
    print(f"money: {profit}$")
order = True
while order:
    flavor = input("What would you like? (espresso/latte/cappuccino):\n").lower()
    if flavor == 'off':
        order = False
    elif flavor == 'report':
        display_report()
    elif flavor == 'espresso' or flavor == 'latte' or flavor == 'cappuccino':
        order = check_ingredients(flavor)

        if order:
            process_coins(flavor)


