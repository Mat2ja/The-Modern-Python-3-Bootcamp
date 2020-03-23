from random import randint
player_wins = 0
computer_wins = 0
winning_score = 3
#winning_score = int(input("First to "))

# for time in range(3): # ako hocemo odredeni broj igara
while player_wins < winning_score and computer_wins < winning_score:
    print(f"Player Score: {player_wins} Computer Score: {computer_wins}\n")
    print("\t...rock...")
    print("\t...paper...")
    print("\t...scissors...")

    player = input("\n(Enter your choice): ").lower()
    if player == "quit" or player == "q":
        break
    random_num = randint(0, 2)
    
    if (random_num == 0):
        computer = "rock"
    elif (random_num == 1):
        computer = "paper"
    else:
        computer = "scissors"

    print(f"The computer plays: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock":
        if computer == "paper":
            print("Computer wins :( ")
            computer_wins += 1
        else:
            print("Player wins!")
            player_wins += 1
    elif player == "paper":
        if computer == "rock":
            print("Player win!")
            player_wins += 1
        else:
            print("Computer wins!")
            computer_wins += 1
    elif (player == "scissors"):
        if (computer == "rock"):
            print("Computer wins!")
            computer_wins += 1
        else:
            print("You win!")
            player_wins += 1
    else:
        print("Please enter a valid move!")

    print("\n")

if player_wins > computer_wins:
    print("CONGRATS, YOU WON!")
elif player_wins == computer_wins:
    print("IT'S A TIE")
else:
    print("OH NO :( THE COMPUTER WON...")


# ja samo dodao \n i \t
