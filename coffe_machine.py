MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk":0,
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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}








def report():
    print(f"water: {resources["water"]}ml")
    print(f"milk: {resources["milk"]}ml")
    print(f"coffee: {resources["coffee"]}g")


def process_coins(menu1, order1):

# quarters = 0.25
# dimes = 0.10 
# nickles = 0.05
# pennies = 0.01
    a=int(input("insert quarters: "))
    b=int(input("insert dimes: "))
    c=int(input("insert nickles: "))
    d=int(input("insert pennies: "))
    quarters=0.25*a
    dimes=0.10*b
    nickles=0.05*c
    pennies=0.01*d
    all = quarters + dimes * 2 + nickles + pennies * 2
    if all>menu1[order1]["cost"]:
        all-=menu1[order1]["cost"]
        rounded=round(all,2)
        print(f"here is your change ${rounded} ")
    else:
        Check_transaction(menu1,order1)


def Check_transaction(menu1,order1):
    print("Sorry that's not enough money. Money refunded.")
    process_coins(menu1, order1)        


def make_coffee(resources1, menu1, order1):
    resources1["coffee"]-= menu1[order1]["ingredients"]["coffee"]
    resources1["water"]-= menu1[order1]["ingredients"]["water"]
    resources1["milk"]-= menu1[order1]["ingredients"]["milk"]
    print(f"Here is your {order1}")




def resourcesv(resources1, menu1,order1,score1):
        if order1=="report":
            report()
        else:
            if resources1["water"] >menu1[order1]["ingredients"]["water"]:
                if resources1["milk"] >menu1[order1]["ingredients"]["milk"]:
                    if resources1["coffee"] > menu1[order1]["ingredients"]["coffee"]:
                            process_coins(menu1, order1)
                            make_coffee(resources1=resources, menu1=MENU,order1=order)
                    else:
                        print("Sorry there is not enough water.")
                else:
                        print("Sorry there is not enough milk.")
            else:
                    print("Sorry there is not enough water.")

score=0
while score==0:
    order=input("What would you like? (espresso/latte/cappuccino):\n")
    if order=="off":
        score+=10
    else:
        resourcesv(resources1=resources, menu1=MENU,order1=order,score1=score)




print()


