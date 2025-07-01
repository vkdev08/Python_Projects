from random import randint

def game(ans,attempts):
    
    while attempts>0:
        print(f"You have {attempts} attempts remaining to guess the number")
        num = int(input("Make a Guess: "))
        attempts -= 1
        if num>ans:
            print("Too High")
        elif num< ans:
            print("Too Low")
        else:
            print(f"You got it!!, the answer was {ans}.")
            return 
        if attempts != 0:
            print(f"Guess Again.")
    print("You have completed all the attempts")
    print(f"The correct answer was {ans}")

#game-setup
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 to 100.")

#game-setup variable
ans = randint(1,100)
EASY = 10
HARD = 5

#game
s = input("Choose Difficulty. Type 'easy' or 'hard': ")
if s == 'easy':
    game(ans,EASY)
elif s == 'hard':
    game(ans,HARD)
else:
    print("Enter a valid option")