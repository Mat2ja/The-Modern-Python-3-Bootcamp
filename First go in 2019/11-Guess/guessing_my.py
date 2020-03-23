import random

random_number = random.randint(1,10)
guess = None

while guess != random_number:
    guess = int(input("Guess a number from 1 to 10: "))
    if guess < random_number:
        print("Too low, try again!")
    elif guess > random_number:
        print("Too high, try again")
    else:
        print("You guessed it! You won!")
    
    
