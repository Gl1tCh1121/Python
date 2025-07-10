import sys
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost":1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost":2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 50,
            "milk": 100,
            "coffee": 24,
        },
        "cost":3.0,
    }
}
resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
        "money": 0.0,
    }

def coffee_machine():  
    
    report = input("What would you like? (espresso/latte/cappuccino):").lower()

    def resources_checker():
        for item, amount in resources.items():
            if item == "money":
                return True            
            if MENU[report]["ingredients"][item] > amount:
                print(f'Sorry there is not enough {item}.')
                coffee_machine()
                return        
        return True
    def resouses_counter():
        for item in resources.items():
            if item == "money":
                return            
            resources[item] -= MENU[report]["ingredients"][item]     
        return

    if report == "report":
        print(f"Water: {resources['water']}ml\n"
            f"Milk: {resources['milk']}ml\n"
            f"Coffee: {resources['coffee']}g\n"
            f"Money: ${resources['money']}\n")
        coffee_machine()
        return
    elif report == "off":
        sys.exit()
    elif resources_checker():
        print("please insert coins.")
        quarters = float(input("How many quarters?: ")) * 0.25
        dimes = float(input("How many dimes?: ")) * 0.1
        nickles = float(input("How many nickles?: ")) * 0.05
        pennies = float(input("How many pennies?: ")) * 0.01
        total = quarters + dimes + nickles + pennies

        if MENU[report]["cost"] < total:
            change = total - MENU[report]["cost"]
            resources['money'] += total - change
            print(f"Here is ${round(change,3)} your change.")
            print(f"Here is your {report} ☕ Enjoy!")
            resouses_counter()
            coffee_machine()
        elif MENU[report]["cost"] == total:
            resources['money'] += total
            print(f"Here is your {report} ☕ Enjoy!")
            resouses_counter()
            coffee_machine()
        else:
            print("Sorry that's not enough money. Money refunded.")
            coffee_machine()


coffee_machine()

