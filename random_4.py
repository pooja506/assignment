import random #importing random module to generate random numbers

randomNumber=(random.randint(1,7)) #random numbers between 1-7

def guess():
    print("Guessing Game")
    userNumber= input("Guess your number: ") 
    if randomNumber==userNumber: #comparing the random number and the user guessed number
        print("You have guessed right number ")
    else:
        print(f"Sorry, correct guess number was {randomNumber}")

guess() #calling the guess fuction

i = input("Press \"Y\" to play again, or \"Q\" to quit") 
if i=='Y': 
    guess() #calling the guess function if user enters Y



