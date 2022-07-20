from Board import Board

def MinMax(board: Board, depth: int, isHumanTurn: bool, maximizing: bool = True, alpha: int = -1000000, beta: int = 1000000):
    # base case
    if depth == 0 or board.gameFinished():
        # We add the depth as an incentive to choose the branch that is shorter
        return board.getHueristic(isHumanTurn) + depth, None, None
    
    # if the player is the computer (maximizing)
    if maximizing:
        maximum, betterSource, betterDestination = float('-inf'), None, None
        for holeSource in board.getComputerHole():
            for holeDestination in board.getAllValidMoves(holeSource):
                # play a move
                board.moveBall(holeSource, holeDestination)
                # call MinMax recursively to walk down the tree
                resPoints, _1, _2 = MinMax(board, depth - 1, False, not maximizing, alpha, beta)
                # undo the move
                board.moveBall(holeDestination, holeSource)
                # update the maximum
                if resPoints > maximum:
                    maximum, betterSource, betterDestination = resPoints, holeSource, holeDestination
                # update the alpha
                alpha = max(alpha, resPoints)
                # prune the tree upon reaching the beta
                if beta <= alpha:
                    break
            # prune the tree upon reaching the beta
            if beta <= alpha:
                break
        # return the best move
        return maximum, betterSource, betterDestination

    # if the player is the human (minimizing)
    else:
        minPoints, betterSource, betterDestination = float('inf'), None, None
        for holeSource in board.getPlayerHole():
            for holeDestination in board.getAllValidMoves(holeSource):
                # play a move
                board.moveBall(holeSource, holeDestination)
                # call MinMax recursively to walk down the tree
                resPoints, _1, _2 = MinMax(board, depth - 1, True, not maximizing, alpha, beta)
                # undo the move
                board.moveBall(holeDestination, holeSource)
                # update the minimum
                if resPoints < minPoints:
                    minPoints, betterSource, betterDestination = resPoints, holeSource, holeDestination
                # update the beta
                beta = min(beta, resPoints)
                # prune the tree upon reaching the beta
                if beta <= alpha:
                    break
            # prune the tree upon reaching the beta
            if beta <= alpha:
                break
        # return the best move
        return minPoints, betterSource, betterDestination
