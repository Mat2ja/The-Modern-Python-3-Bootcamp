from random import randint

picks = ["rock", "paper", "scissors"]

draw_msg = "\nIt's a draw"
win1_msg = "\nPlayer 1 wins!"
win2_msg = "\nPlayer 2 wins!"
win3_msg = "\nPlayer wins!"
win4_msg = "\nComputer wins!"
error_msg = "\nSomething went wrong"
#msg = None

#Players: player, computer, player1, player2

print("LET'S PLAY ROCK-PAPER-SCISSORS!!!")

print("Choose a game mode:\n" +
        "\t- Player vs Computer (1)\n" + 
        "\t- Multiplayer (2)")
mode = int(input(">>>>> "))

for pick in picks:
    print(f"\n{pick}...")
print()

while True:
    if mode == 1: # player vs computer
        rand_num = randint(0,2)
        if rand_num == 0:
            computer = "rock"
        elif rand_num == 1:
            computer = "paper"
        else:
	        computer = "scissors"
        player = input("Player, choose your pick > ")
        print(f"Computer player {computer}") # shows what computer chose
        player1 = player # player becomes player1
        player2 = computer # computer becomes player2
    elif mode == 2: # multiplayer
        player1 = input("Player 1, choose your pick > ")
        print("\t\n##### NO CHEATING #####\n\n" * 20)
        player2 = input("Player 2, choose your pick > ")
    else:
        break

    if player1 == "quit" or player2 == "quit":
        break

    if player1 in picks and player2 in picks: # checks if both player chose valid picks
        if player1 == player2:
                msg = draw_msg
        elif player1 == "rock":
            if player2 == "paper":
                msg = win2_msg
            elif player2 == "scissors":
                msg = win1_msg
        elif player1 == "paper":
            if player2 == "rock":
                msg = win1_msg
            elif player2 == "scissors":
                msg = win2_msg
        elif player1 == "scissors":
            if player2 == "rock":
                msg = win2_msg
            elif player2 == "paper":
                msg = win1_msg
    else: # if any of the picks is invalid
        if mode == 1 and msg != draw_msg:
            win1_msg = win3_msg
            win2_msg = win4_msg
        msg = error_msg;

    print(msg) # PRINTS THE OUTCOME
    
    answer = input("\nPlay another? (y/n) > ")
    
    if answer[0] != "y": # ends the game
        print("\t\nTHANK YOU FOR PLAYING!\n")
        break; # breaks out of the while loop


    