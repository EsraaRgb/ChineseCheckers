from BoardComponents import *
from BoardUtils import *

CHARACTERS = "123456789ABCDEFGHJKLMNPQRSTUVWXYZ"


# State Representation Class

class Board():

    # puts the balls in the holes
    def defineBoardRows(self):
        holesRow = [
            1, 2, 3, 4,
            13, 12, 11, 10, 9, 10, 11, 12, 13,
            4, 3, 2, 1
        ]
        boardRows = []
        for i in range(len(holesRow)):
            boardRows.append([Hole() for x in range(holesRow[i])])
        return boardRows

    # store the board as one row to iterate over them
    def serializeBoard(self):
        board = []
        for row in self.eachRow:
            board.extend(row)
        return board

    # Evaluation function
    # hueristic function to evaluate the board from prespective of each player

    def evaluateBoardHueristic(self):
        # Calculate scores for human player
        tempTraversing = [self.serializedBoard[-1]]
        # set the initial hureistic to the distance between the last two holes on the board
        tempTraversing[0].setHeuristicForHuman(16)
        while any(tempTraversing):
            holeTraversed, tempTraversing = tempTraversing[0], tempTraversing[1:]
            tempTraversing.extend([tile for tile in holeTraversed.getAdjacents().values() if
                                   tile.setHeuristicForHuman(holeTraversed.humanHeuristic - 1)])
        for Hole in self.greenTriangleHoles():
            Hole.setHeuristicForHuman(5 + Hole.humanHeuristic)

        # Calculate Heuristic for computer player
        tempTraversing = [self.serializedBoard[0]]
        # set the initial Heuristic to the distance between the last two holes on the board
        tempTraversing[0].setHeuristicForComputer(16)
        while any(tempTraversing):
            holeTraversed, tempTraversing = tempTraversing[0], tempTraversing[1:]
            tempTraversing.extend([tile for tile in holeTraversed.getAdjacents().values() if
                                   tile.setHeuristicForComputer(holeTraversed.computerHeuristic - 1)])
        for Hole in self.redTriangleHoles():
            Hole.setHeuristicForComputer(5 + Hole.computerHeuristic)

    # initialize the 10 balls for each player
    def putBallsOnBoard(self) -> None:
        ballIndex = 0
        for ball in self.redBalls:
            self.serializedBoard[ballIndex].setBall(ball)
            ballIndex += 1

        for ball in self.greenBalls:
            self.serializedBoard[-ballIndex].setBall(ball)
            ballIndex -= 1

    def __init__(self) -> None:
        self.eachRow = self.defineBoardRows()
        self.serializedBoard: list[Hole] = self.serializeBoard()
        self.redBalls = [Ball("R") for i in range(10)]
        self.greenBalls = [Ball("G") for i in range(10)]
        AddHolesAdjacents(self)
        self.putBallsOnBoard()
        self.evaluateBoardHueristic()

    # def setAdjacentHoles(self) -> None:
    #     # Add adjacents Right and Left within the row
    #
    #

    # get the human player's balls at the current state
    def getPlayerHole(self):
        return filter(lambda t: not t.isEmpty() and t.getBall().playerBall(), self.serializedBoard)

    # get the human computer's balls at the current state
    def getComputerHole(self):
        return filter(lambda t: not t.isEmpty() and t.getBall().computerBall(), self.serializedBoard)

    # check if the human has reached the green triangle
    def humanReachedDestination(self):
        for hole in self.greenTriangleHoles():
            if (hole.isEmpty() or not hole.getBall().playerBall()):
                return False
        return True

    # check if the computer has reached the red triangle
    def computerReachedDestination(self):
        for hole in self.redTriangleHoles():
            if (hole.isEmpty() or not hole.getBall().computerBall()):
                return False
        return True

    # evaluation function
    def getHueristic(self, humanTurn):
        if (humanTurn and self.humanReachedDestination()) or (not humanTurn and self.computerReachedDestination()):
            return 1000000
        if (humanTurn and self.computerReachedDestination()) or (not humanTurn and self.humanReachedDestination()):
            return -1000000

        # calculate the huristics for each player
        humanScore = sum(t.getHeuristic() for t in self.getPlayerHole()) * (1 if humanTurn else -1)
        computerScore = sum(t.getHeuristic() for t in self.getComputerHole()) * (-1 if humanTurn else 1)
        return humanScore + computerScore

    # checks if the game is finished
    def gameFinished(self):
        return self.computerReachedDestination() or self.humanReachedDestination()

    # get the possible moves for the current state
    def possibleMoves(self, Hole, jumps=False, alreadyJumped=None, returned=None):
        # initialize the argumaents
        if alreadyJumped is None:
            alreadyJumped = set()
            returned = set()

        # we dont expect further moves if the hole is already jumped
        if Hole not in alreadyJumped:
            alreadyJumped.add(Hole)

            for (adjacentDirection, adjacentHole) in Hole.getAdjacents().items():
                if adjacentHole.isEmpty():
                    if not jumps:
                        yield adjacentHole
                else:
                    # if the adjacent is not empty, it means we may be able to jump over it
                    adjacentOfAdjacents: Hole = adjacentHole.getAdjacents().get(adjacentDirection, None)
                    if adjacentOfAdjacents is not None:
                        if adjacentOfAdjacents.isEmpty():
                            if adjacentOfAdjacents not in returned:
                                yield adjacentOfAdjacents
                                returned.add(adjacentOfAdjacents)
                            for move in self.possibleMoves(adjacentOfAdjacents, True, alreadyJumped, returned):
                                yield move
                                returned.add(move)

    # return all red holes
    def redTriangleHoles(self):
        return self.serializedBoard[:10]

    # return all green holes
    def greenTriangleHoles(self):
        return self.serializedBoard[-10:]

    # move a ball form source hole to destination hole ( return true if the move is valid )
    def moveBall(self, sourceHole, destinationHole):
        if not destinationHole.isEmpty():
            # the hole is not valid
            return False

        destinationHole.setBall(sourceHole.getBall())
        sourceHole.setEmpty()

        return True

    # return all the valid moves from the selected hole
    def getAllValidMoves(self, sourceHole):
        # prevent any ball to move out of the opponenet's triangle
        for move in self.possibleMoves(sourceHole):
            if sourceHole.getBall().computerBall() and sourceHole in self.redTriangleHoles() and move not in self.redTriangleHoles():
                continue
            elif sourceHole.getBall().playerBall() and sourceHole in self.greenTriangleHoles() and move not in self.greenTriangleHoles():
                continue
            else:
                yield move

    ################## print the board as a whole ##################
    def printBoard(self, holes=None):
        print(self.toString(holes))

    def toString(self, holes=None):
        fullBoard = ""
        holes = [] if holes is None else list(holes)

        maxLength: int = max((len(row) for row in self.eachRow))  # the maximum row length

        fullBoard += "============================\n"
        for row in self.eachRow:
            # Print the spaces before eachs row
            fullBoard += " " * (maxLength - len(row))
            hole = Hole()
            for hole in row:
                if hole in holes:
                    fullBoard += f"{CHARACTERS[holes.index(hole)]} "
                else:
                    fullBoard += f"{str(hole)} "
            fullBoard += "\n"
        fullBoard += "\n"

        return fullBoard
    ##################################################################
