from Board import *
from BoardComponents import Hole

def getPlayerMove(board: Board):
    # get the balls that are able to move
    ballsToMove: list[Hole] = list(filter(
        lambda t: any(board.getAllValidMoves(t)),
        board.getPlayerHole() 
    ))
    board.printBoard(ballsToMove)
    numberOfMovableBalls = len(ballsToMove)
    while True:
        # take the the wanted ball as a user input
        ballIndex = input(f"Select a ball ({CHARACTERS[0]} - {CHARACTERS[numberOfMovableBalls - 1]})")
        ballIndex = ballIndex.strip().upper()
        # check if the entered character is within the range of the balls that can move
        if ballIndex in CHARACTERS[: numberOfMovableBalls]:
            selectedBall = ballsToMove[CHARACTERS.index(ballIndex)]
            return selectedBall

def inputDestinationHole(board: Board, sourceHole: Hole):
    available_holeDestinations: list[Hole] = [tile for tile in board.getAllValidMoves(sourceHole)]

    board.printBoard(available_holeDestinations)

    while True:
        holeIndex = input(
            f"Select a hole to move to ({CHARACTERS[0]} - {CHARACTERS[len(available_holeDestinations) - 1]})").strip().upper()
        if len(holeIndex) != 1:
            continue
        if holeIndex in CHARACTERS[: len(available_holeDestinations)]:
            destination_hole = available_holeDestinations[CHARACTERS.index(holeIndex)]
            return destination_hole
        
