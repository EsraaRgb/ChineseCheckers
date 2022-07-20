from utils import *
from greedy import MinMax


# Green player is the computer
class Computer():
    def __init__(self, name, depth):
        self.name = name
        self.depth = depth
    # calculate the best move through minmax algorithm
    def getMove(self, board):
        maxUtility, sourceHole, destinationHole = MinMax(board, self.depth, False, True)
        return (sourceHole, destinationHole)

# Red player is the computer
class Human():
    def __init__(self, name):
        self.name = name

    def getMove(self, board):
        # Select hole from all holes that contain balls and can be moved
        sourceHole: Hole = getPlayerMove(board)
        # Select the destination hole for the selected ball
        destinationHole: Hole = inputDestinationHole(board, sourceHole)
        return (sourceHole, destinationHole)
