#game variables
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
balance = 0

#Methods
def ingredient_check(coffee_type, resources,MENU):
    """method to check if coffee is available in MENU, and if yes, then checks if the resources are enough to make the required coffee"""
    ingredient_checker = True #to check the ingredients enough to make the required coffee
    if coffee_type not in MENU:
        return False, False
    else:
        coffee_ingredients = MENU[coffee_type]["ingredients"]
        ingredient_checker = all(key in resources and resources[key] >= MENU[coffee_type]['ingredients'][key] for key in MENU[coffee_type]['ingredients'])
    return ingredient_checker,True 

def amt_received_check(coffee_type,amt_received,MENU):
    """method to verify the amt_received is sufficient to make the required coffee"""
    amt_needed = MENU[coffee_type]['cost']
    amt_returned = amt_received - amt_needed
    if amt_returned >= 0:
        if amt_returned > 0:
            print(f"Amount returned: $ {amt_returned:.3f}")
        return True
    else:
        print(f"Amount returned: $ {amt_received:.3f}")
        return False

def make_coffee(coffee_type,MENU,resources):
    """makes the coffee using the available resources"""
    for k in MENU[coffee_type]['ingredients']:
        if k in resources:
            resources[k] -= MENU[coffee_type]['ingredients'][k]
    return resources
    
def process_coins():
    """takes the coins from the user, and calculates the amout"""
    #values of coin processing
    QUARTER_VALUE = 0.25
    DIME_VALUE = 0.10
    NICKEL_VALUE = 0.05 
    PENNY_VALUE = 0.01
    
    #taking input from user
    quarters = int(input("Enter the number of quarters: "))
    dimes = int(input("Enter the number of dimes: "))
    nickles = int(input("Enter the number of nickles: "))
    pennies = int(input("Enter the number of pennies: ")) 
    
    amt_received = quarters*QUARTER_VALUE + dimes*DIME_VALUE + nickles*NICKEL_VALUE + pennies*PENNY_VALUE
    return amt_received

def coffee_machine(balance,resources, MENU):
    """The main logic in processing the coffee"""
    running = True
    
    #user-input
    coffee_type = input("What would you like to have?: ").strip().lower()

    if coffee_type == 'report':
        #print report
        for key in resources:
            print(f"{key.capitalize()}: {resources[key]}")
        print(f"Balance: ${balance:.2f}")
    
    if coffee_type == "off":
        print("Shutting down the Machine... ")
        running = False
        
    else:
        #make coffee
        ingredient_checker, coffee_availability = ingredient_check(coffee_type, resources, MENU)
        if not coffee_availability:
            print("This coffee is not in our menu")
        else:    
            if ingredient_checker:
                amt_received = process_coins()
                if amt_received_check(coffee_type, amt_received,MENU):
                    resources = make_coffee(coffee_type,MENU,resources)
                    print("Please enjoy your", coffee_type)
                    balance += MENU[coffee_type]['cost']
                else:
                    print("Insufficent amout,Please enter the sufficient amount from the menu")
            else:
                print("Insufficient ingredients to process your coffee")
    
    return balance, resources, running

#Machine Loop
running = True
while running:
    #MENU printing
    print("MENU: ")
    for key in MENU:
        print(f"{key.capitalize(): <10}: ${MENU[key]['cost']:>6.3f}")
        
    #coffee macking
    balance, resources,running = coffee_machine(balance,resources,MENU)
    print("\n")