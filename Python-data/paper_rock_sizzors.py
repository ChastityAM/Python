import sys

player1 = input("Enter your choice in letter form (rock r / paper p / scissors s) : \n")

if (player1 == "s"):
        player1 = "scissors"
elif (player1 == "r"):
        player1 = "rock"
elif (player1 == "p"):
        player1 = "paper"
else:
    print("Invalid Input Quitting...")
    sys.exit(0)

player2 = input("Enter your choice in number (rock r / paper p / scissors s) : \n")

if (player2 == "s"):
        player2 = "scissors"
elif (player2 == "r"):
        player2 = "rock"
elif (player2 == "p"):
        player2 = "paper"
else:
    print("Invalid Input Quitting...")
    sys.exit(0)

if (player1 == player2):
        print("Player1 is ",player1, "Player2 is ",player2," You Draw!")

elif (player1 == "rock"):
    if (player2 == "paper"):
            print("Player 1 is ",player1, "Player 2 is ",player2," Player 2 Wins!")
    else:
            print("Player 1 is ",player1, "Player 2 is ",player2," Player 1 Wins!")

elif (player1 == "paper"):
    if (player2 == "rock"):
            print("Player 1 is ",player1, "Player 2 is ",player2," Player 1 Wins!")
    else:
            print("Player 1 is ",player1, "Player 2 is ",player2," Player 2 Wins!")

elif (player1 == "scissors"):
    if (player2 == "rock"):
            print("Player1 is ",player1, "Player2 is ",player2," Player 2 Wins!")
    else:
            print("Player1 is ",player1, "Player2 is ",player2, "Player 1 Wins!")


