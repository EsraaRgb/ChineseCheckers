def AddHolesAdjacents(board):
    AddRowAdjacents(board)
    addAdjacent1(board)
    addAdjacent2(board)
    addAdjacent3(board)
    addAdjacent4(board)


# Add Left And Right Adjacents within the Row
def AddRowAdjacents(board):
    for row in board.eachRow:
        for i in range(0, len(row) - 1):
            row[i].setAdjacent("R", row[i + 1])
        for i in range(1, len(row)):
            row[i].setAdjacent("L", row[i - 1])


# for this Hole Add the Down left Adjacent and Down Right adjacent
# for next Row put this Hole as  Upper Right adjacent for one Hole and Upper left Adjacent for The another Hole
def addAdjacent1(board):
    for rowIndex in [0, 1, 2, 8, 9, 10, 11]:
        for holeIndex in range(len(board.eachRow[rowIndex])):
            board.eachRow[rowIndex][holeIndex].setAdjacent("DL", board.eachRow[rowIndex + 1][holeIndex])
            board.eachRow[rowIndex][holeIndex].setAdjacent("DR", board.eachRow[rowIndex + 1][holeIndex + 1])
            board.eachRow[rowIndex + 1][holeIndex].setAdjacent("UR", board.eachRow[rowIndex][holeIndex])
            board.eachRow[rowIndex + 1][holeIndex + 1].setAdjacent("UL", board.eachRow[rowIndex][holeIndex])

# for this given rows Add  the upper left and right for this hole
# and for the row before Add this hole as down right for one and down left for other
def addAdjacent2(board):
    for rowIndex in [5, 6, 7, 8, 14, 15, 16]:
        for holeIndex in range(len(board.eachRow[rowIndex])):
            board.eachRow[rowIndex][holeIndex].setAdjacent("UL", board.eachRow[rowIndex - 1][holeIndex])
            board.eachRow[rowIndex][holeIndex].setAdjacent("UR", board.eachRow[rowIndex - 1][holeIndex + 1])
            board.eachRow[rowIndex - 1][holeIndex].setAdjacent("DR", board.eachRow[rowIndex][holeIndex])
            board.eachRow[rowIndex - 1][holeIndex + 1].setAdjacent("DL", board.eachRow[rowIndex][holeIndex])

#  Exception Cases for Row index 3 , 4

def addAdjacent3(board):
    for holeIndex in range(len(board.eachRow[3])):
        board.eachRow[4][holeIndex + 4].setAdjacent("UR", board.eachRow[3][holeIndex])
        board.eachRow[4][holeIndex + 5].setAdjacent("UL", board.eachRow[3][holeIndex])
        board.eachRow[3][holeIndex].setAdjacent("DL", board.eachRow[4][holeIndex + 4])
        board.eachRow[3][holeIndex].setAdjacent("DR", board.eachRow[4][holeIndex + 5])

#  Exception Cases for Row index 12, 13

def addAdjacent4(board):
    for holeIndex in range(len(board.eachRow[13])):
        board.eachRow[13][holeIndex].setAdjacent("UL", board.eachRow[12][holeIndex + 4])
        board.eachRow[13][holeIndex].setAdjacent("UR", board.eachRow[12][holeIndex + 5])
        board.eachRow[12][holeIndex + 4].setAdjacent("DR", board.eachRow[13][holeIndex])
        board.eachRow[12][holeIndex + 5].setAdjacent("DL", board.eachRow[13][holeIndex])
