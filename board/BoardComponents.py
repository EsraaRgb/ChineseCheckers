class Ball():
    def __init__(self, color: str) -> None:
        self.color: str = color

    def __str__(self) -> str:
        return self.color

    # returns true if the ball is a player ball
    def computerBall(self) -> bool:
        return self.color == "G"
    # returns true if the ball is a computer ball
    def playerBall(self) -> bool:
        return self.color == "R"

class Hole():
    Directions: list[str] = ["L", "R", "UL", "UR", "DL", "DR"]
    emptyHoleStr: str = "-"
    baseHeuristic: int = -1

    def __init__(self) -> None:
        self.ball = None
        self.adjacents: dict[str, Hole] = {}
        self.humanHeuristic: int = Hole.baseHeuristic
        self.computerHeuristic: int = Hole.baseHeuristic

    def __str__(self) -> str:
        return Hole.emptyHoleStr if self.isEmpty() else str(self.getBall())

    def setBall(self, newBall: Ball) -> None:
        self.ball = newBall

    def getBall(self) -> Ball:
        return self.ball

    def setEmpty(self) -> None:
        self.setBall(None)

    def isEmpty(self) -> bool:
        return self.getBall() is None

    def setHeuristicForHuman(self, newHeuristic: int) -> bool:
        if self.humanHeuristic == Hole.baseHeuristic or (newHeuristic > self.humanHeuristic):
            self.humanHeuristic = newHeuristic
            return True
        return False

    def setHeuristicForComputer(self, newHeuristic: int) -> bool:
        if self.computerHeuristic == Hole.baseHeuristic or (newHeuristic > self.computerHeuristic):
            self.computerHeuristic = newHeuristic
            return True
        return False

    def getHeuristic(self) -> int:
        if self.getBall().computerBall():
            return self.computerHeuristic
        else:
            return self.humanHeuristic

    def setAdjacent(self, direction: str, adjacentHole) -> None:
        self.adjacents[direction] = adjacentHole

    def getAdjacents(self) -> dict:
        return self.adjacents
