from art import logo,vs
from game_data import data
from random import randint

#score
score = 0

#game-setup variables
running = True
a = randint(0,len(data)-1)

def validate_score(A,B,n,score):
    """updates score if corrent and returns score else ends the game"""
    if n == 'A' and A>B:
        return True,score + 1
    elif n == 'B' and B>A:
        return True,score + 1
    else:
        return False,score

#Game Loop
while running :
    print(logo)
    A = f"{data[a]['name']}, a {data[a]['description']}, from {data[a]['country']}"
    A_f = data[a]["follower_count"]
    print("Compare A: " + A)
    b = randint(0,len(data)-1)
    while a == b:
        b = randint(0,len(data)-1)
    print(vs)
    B = f"{data[b]['name']}, a {data[b]['description']}, from {data[b]['country']}" 
    B_f = data[b]["follower_count"]
    print("Against B: " + B)
    n = input("Who has more followers? Type 'A' or 'B': ")
    if n not in['A','B']:
        print("Invalid input, try again !!")
        continue
    running,score = validate_score(A_f,B_f,n,score)
    if running:
        print(f"You're right! Current score: {score}")
        print('\n'*20)
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
    if A_f < B_f :
        a = b
    
    