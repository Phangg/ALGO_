import sys

# 행 체크
def rowCheck(r, num):
    for c in range(9):
        if board[r][c] == num:
            return False
    return True

# 열 체크
def colCheck(c, num):
    for r in range(9):
        if board[r][c] == num:
            return False
    return True

# 3 * 3 사각형 체크
def boxcheck(r, c, num):
    start_r, start_c = (r//3)*3, (c//3)*3
    for x in range(3):
        for y in range(3):
            if board[start_r + x][start_c + y] == num:
                return False
    return True

# 비어있는 좌표들 하나씩 진행
def dfs(n):
    if n == len(blanks):
        for x in range(9):
            for y in range(9):
                print(board[x][y], end="")
            print()
        exit()

    now_row, now_col = blanks[n]
    for num in range(1, 10):
        if rowCheck(now_row, num) and colCheck(now_col, num) and boxcheck(now_row, now_col, num):
            board[now_row][now_col] = num
            dfs(n+1)
            board[now_row][now_col] = 0

board = []
blanks = []
for i in range(9):
    board.append(list(map(int, sys.stdin.readline().strip())))
    for j in range(9):
        if board[i][j] == 0:
            blanks.append((i, j))

dfs(0)