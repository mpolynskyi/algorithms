print("Enter the number of players")
N = int(input())

# NxN matrix with all elements 0
board = [[0] * N for _ in range(N)]


def is_under_attack(row, col):
    # checking if there is a player in row or column
    for k in range(N):
        if board[row][k] == 1 or board[k][col] == 1:
            return True
    # checking diagonals
    for r in range(N):
        for c in range(N):
            # https://math.stackexchange.com/questions/1194565/how-to-know-if-two-points-are-diagonally-aligned
            if abs(r-row) == abs(c - col):
                if board[r][c] == 1:
                   return True
    return False


def N_players(n):
    # if n is 0, solution found
    if n == 0:
        return True
    for r in range(N):
        for c in range(N):
            # check if we can place player
            if (not (is_under_attack(r, c))) and (board[r][c] != 1):
                board[r][c] = 1
                # recursion
                # check if it possible to place other players with already created placement
                if N_players(n - 1) == True:
                    return True
                board[r][c] = 0
    # for i in board:
    #     print(i)
    # print("\n")
    return False


N_players(N)
for i in board:
    print(i)
