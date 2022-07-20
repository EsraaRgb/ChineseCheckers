from __future__ import annotations
from Players  import *


# main game scenarios go here
# GameHandler Handle Turns between Player and Computer
if __name__ == "__main__":
    # initialize the board
    board = Board()
    # create the human player
    human = Human("Player1")

    # take the difficulty as a user input
    difficulty = input("\nWhich difficulty? (E)asy,(M)edium,(H)ard: ").strip().lower()
    while difficulty not in ["m", "h", "e"]:
        difficulty = input("please enter e, m or h: ").strip().lower()
    computer = None

    # check the difficulty to create the computer player with the correct depth
    if difficulty == "e":
        computer = Computer("Player2", 1)
    elif difficulty == "m":
        computer = Computer("Player2", 3)
    elif difficulty == "h":
        computer = Computer("Player2", 5)
    
    # store the players in a list to make them take turns depending on nextPlayer
    players = (human,computer)
    nextPlayer = 0
    
    # start the game logic
    if players[nextPlayer] == human:
        print("Human moves First")
    else:
        print("Computer Moves First")
    while not board.gameFinished():
        player = players[nextPlayer]
        if players[nextPlayer] == computer:
            print("\nComputer is thinking...")
        holeOrigin, holeDestination = player.getMove(board)
        board.moveBall(holeOrigin, holeDestination)
        board.printBoard()
        nextPlayer = (nextPlayer + 1) % len(players)

    # print the winner
    if board.humanReachedDestination():
        print("Player has won")
    else:
        print("Computer has won")
