from random import randint

random_number = randint(1,10);
counter = 0;
all_guesses = []
# guess = None

while True:
    guess = input("Guess a number between 1 and 10: ")
    guess = int(guess)
    counter += 1
    all_guesses.append(guess)

    if guess < random_number:
        print("Too low, try again")
    elif guess > random_number:
        print("Too high, try again")
    else:
        print(f"You guessed it in {counter} tries! You won!!!")
        print("Your guesses were: " + str(all_guesses))

        play_again = input("Do you want to keep playing? (y/n): ")
        if play_again[0] == 'y':
            random_number = randint(1,10)  # numbers 1 - 10
            # guess = None
            counter = 0
            all_guesses = []

        else:
            print("Thank you for playing my awful game :)")
            break