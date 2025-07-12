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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def ingredient_check(coffee_type, resources,MENU):
    checker = True
    if coffee_type not in MENU:
        print("Please enter a valid input")
        checker = False    
    else:
        coffee_ingredients = MENU[coffee_type]["ingredients"]
        checker = all(key in resources and resources[key] >= MENU[coffee_type]['ingredients'][key] for key in MENU[coffee_type]['ingredients'])
    return checker 

def amt_check(coffee_type,amt,MENU):
    amt_needed = MENU[coffee_type]['cost']
    amt_returned = amt - amt_needed
    if amt_returned >= 0:
        return True
    else:
        return False


def make_coffee(coffee_type,MENU,resources):
    for k in MENU[coffee_type]['ingredients']:
        if k in resources:
            resources[k] -= MENU[coffee_type]['ingredients'][k]
    return resources
    
    
def coffee_machine(balance,resources, MENU):
    coffee_type = input("Please enter coffee-type: ").strip().lower()
    if coffee_type == 'report':
        for key,value in resources.items():
            print(key,value)
        print("Balance:", balance)
    else:
        if ingredient_check(coffee_type, resources, MENU):
            quaters = int(input("Enter the number of quaters: "))
            dimes = int(input("Enter the number of dimes: "))
            nickles = int(input("Enter the number of nickles: "))
            pennies = int(input("Enter the number of pennies: "))
            amt = quaters*0.25 + dimes*0.20 + nickles*0.10 + pennies*0.01
            if amt_check(coffee_type, amt,MENU):
                resources = make_coffee(coffee_type,MENU,resources)
                balance += MENU[coffee_type]['cost']
            else:
                print("Insufficent amout")
        else:
            print("We are out of ingredients")
    
    return balance, resources
balance = 0
while True:
    balance, resources = coffee_machine(balance,resources,MENU)
    
# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }

# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }

# def ingredient_check(coffee_type, resources, MENU):
#     if coffee_type not in MENU:
#         print("Please enter a valid input")
#         return False
    
#     coffee_ingredients = MENU[coffee_type]["ingredients"]
    
#     # Check if all ingredients are available in sufficient amounts
#     for ingredient, amount_needed in coffee_ingredients.items():
#         if ingredient not in resources or resources[ingredient] < amount_needed:
#             print(f"We are out of {ingredient}")
#             return False
            
#     return True 

# def amt_check(coffee_type, amt, MENU):
#     amt_needed = MENU[coffee_type]['cost']
#     amt_returned = amt - amt_needed
#     return amt_returned >= 0

# def make_coffee(coffee_type, MENU, resources):
#     for k in MENU[coffee_type]['ingredients']:
#         resources[k] -= MENU[coffee_type]['ingredients'][k]
#     return resources
    
# def coffee_machine(balance, resources, MENU):
#     coffee_type = input("Please enter coffee-type: ").strip().lower()
#     if coffee_type == 'report':
#         for key, value in resources.items():
#             print(key, value)
#         print("Balance:", balance)
#     else:
#         if ingredient_check(coffee_type, resources, MENU):
#             quaters = int(input("Enter the number of quaters: "))
#             dimes = int(input("Enter the number of dimes: "))
#             nickles = int(input("Enter the number of nickles: "))
#             pennies = int(input("Enter the number of pennies: "))
#             amt = quaters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
#             if amt_check(coffee_type, amt, MENU):
#                 resources = make_coffee(coffee_type, MENU, resources)
#                 balance += MENU[coffee_type]['cost']
#             else:
#                 print("Insufficient amount")
#         else:
#             print("We are out of ingredients")
    
#     return balance, resources

# while True:
#     balance = 0
#     balance, resources = coffee_machine(balance, MENU, resources)



# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }

# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }

# def ingredient_check(coffee_type, resources, MENU):
#     if coffee_type not in MENU:
#         print("Please enter a valid input")
#         return False
    
#     for ingredient, needed in MENU[coffee_type]["ingredients"].items():
#         if resources.get(ingredient, 0) < needed:
#             print(f"Sorry, there is not enough {ingredient}")
#             return False
#     return True

# def amt_check(coffee_type, amt, MENU):
#     return amt >= MENU[coffee_type]['cost']

# def make_coffee(coffee_type, MENU, resources):
#     for ingredient, amount in MENU[coffee_type]["ingredients"].items():
#         resources[ingredient] -= amount
#     print(f"Here is your {coffee_type} ☕. Enjoy!")
#     return resources
    
# def coffee_machine(balance, resources, MENU):
#     coffee_type = input("What would you like? (espresso/latte/cappuccino): ").lower()
    
#     if coffee_type == "report":
#         print(f"Water: {resources['water']}ml")
#         print(f"Milk: {resources['milk']}ml")
#         print(f"Coffee: {resources['coffee']}g")
#         print(f"Money: ${balance}")
#         return balance, resources
#     elif coffee_type == "off":
#         exit()
#     elif coffee_type in MENU:
#         if ingredient_check(coffee_type, resources, MENU):
#             print("Please insert coins.")
#             quarters = int(input("How many quarters?: ")) * 0.25
#             dimes = int(input("How many dimes?: ")) * 0.10
#             nickles = int(input("How many nickles?: ")) * 0.05
#             pennies = int(input("How many pennies?: ")) * 0.01
#             total = quarters + dimes + nickles + pennies
            
#             if total >= MENU[coffee_type]['cost']:
#                 change = round(total - MENU[coffee_type]['cost'], 2)
#                 if change > 0:
#                     print(f"Here is ${change} in change.")
#                 balance += MENU[coffee_type]['cost']
#                 resources = make_coffee(coffee_type, MENU, resources)
#             else:
#                 print("Sorry that's not enough money. Money refunded.")
#         else:
#             return balance, resources
#     else:
#         print("Please enter a valid selection")
#         return balance, resources
    
#     return balance, resources

# balance = 0
# while True:
#     balance, resources = coffee_machine(balance, resources, MENU)
 