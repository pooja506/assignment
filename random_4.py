import random

randomNumber=(random.randint(1,7))
def guess():
    print("Guessing Game")
    userNumber= input("Guess your number: ")
    if randomNumber==userNumber:
        print("You have guessed right number ")
    else:
        print(f"Sorry, correct guess number was {randomNumber}")
guess()
i = input("Press \"Y\" to play again, or \"Q\" to quit") 
if i=='Y':
    guess()



