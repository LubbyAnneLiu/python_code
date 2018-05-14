#201721198590   信息科学学院   刘璐
#回溯法解决N皇后问题

global N
N = 4


def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end="")
        print()
    print()


def isSafe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solveNQUtil(board, col):
    if col >= N:
        printSolution(board)
    else:
        for i in range(N):
            if isSafe(board, i, col):
                board[i][col] = 1
                solveNQUtil(board, col + 1)
                board[i][col] = 0
        return False


def solveNQ():

    board = [[0 for i in range(N)] for j in range(N)]

    if not solveNQUtil(board, 0):
        print("Solution does not exist")
        return False

    printSolution(board)
    return True


if __name__ == "__main__":
solveNQ()
