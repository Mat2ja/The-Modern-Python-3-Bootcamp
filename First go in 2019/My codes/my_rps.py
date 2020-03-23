from random import randint
player_wins = 0
computer_wins = 0
winning_score = int(input("\nFirst to > "))

player = None

while True:
    while player_wins < winning_score and computer_wins < winning_score:
        print(
            f"\n(Player Score) {player_wins} : {computer_wins} (Computer Score)\n")
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

        print(f"The computer plays:  {computer}\n")

        if player == computer:
            print("\tIt's a tie!")
        elif player == "rock":
            if computer == "paper":
                print("\tComputer wins :( ")
                computer_wins += 1
            else:
                print("\tPlayer wins!")
                player_wins += 1
        elif player == "paper":
            if computer == "rock":
                print("\tPlayer wins!")
                player_wins += 1
            else:
                print("\tComputer wins :( ")
                computer_wins += 1
        elif (player == "scissors"):
            if (computer == "rock"):
                print("\tComputer wins :( ")
                computer_wins += 1
            else:
                print("\tPlayer wins")
                player_wins += 1
        else:
            print("Please enter a valid move!")

    if player_wins > computer_wins:
        print("\nCONGRATS, YOU WON!\n")
    elif player_wins == computer_wins:
        print("\nIT'S A TIE\n")
    else:
        print("\nOH NO :( THE COMPUTER WON...\n")

    # if player == "quit" or player == "q":
    #    print("###### Thank you for playing :) ######\n")
    #    break

    play_again = input("Do you wanna play again? (y/n) > ")
    if play_again == "y":
        player_wins = 0
        computer_wins = 0
        winning_score = int(input("\nFirst to > "))
    elif play_again == "n" or player == "quit" or player == "q":
        print("\n###### Thank you for playing :) ######\n")
        break
