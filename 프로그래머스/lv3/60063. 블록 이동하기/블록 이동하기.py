from collections import deque

def next_coordinate(coordinate, new_b):
    N = len(new_b)
    next_c_lst = []
    coordinate = list(coordinate)
    x1, y1, x2, y2 = coordinate[0][0], coordinate[0][1], coordinate[1][0], coordinate[1][1]
    for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        nx1, ny1, nx2, ny2 = x1+dx, y1+dy, x2+dx, y2+dy
        if (new_b[nx1][ny1] == 0) and (new_b[nx2][ny2] == 0):
            next_c_lst.append({(nx1, ny1), (nx2, ny2)})

    # 가로
    if x1 == x2:
        if (new_b[x1 - 1][y1] == 0) and (new_b[x2 - 1][y2] == 0):
            next_c_lst.append({(x1, y1), (x1-1, y1)})
            next_c_lst.append({(x2, y2), (x2-1, y2)})
        if (new_b[x1 + 1][y1] == 0) and (new_b[x2 + 1][y2] == 0):
            next_c_lst.append({(x1, y1), (x1+1, y1)})
            next_c_lst.append({(x2, y2), (x2+1, y2)})
    # 세로
    elif y1 == y2:
        if (new_b[x1][y1 - 1] == 0) and (new_b[x2][y2 - 1] == 0):
            next_c_lst.append({(x1, y1), (x1, y1 - 1)})
            next_c_lst.append({(x2, y2), (x2, y2 - 1)})
        if (new_b[x1][y1 + 1] == 0) and (new_b[x2][y2 + 1] == 0):
            next_c_lst.append({(x1, y1), (x1, y1 + 1)})
            next_c_lst.append({(x2, y2), (x2, y2 + 1)})

    return next_c_lst


def solution(board):
    n = len(board)
    new_b = [[1] * (n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            new_b[i+1][j+1] = board[i][j]
    # print(new_b)
    q = deque()
    visited = []
    start = {(1, 1), (1, 2)}
    q.append((start, 0))
    visited.append(start)
    while q:
        coordinate, sec = q.popleft()
        if (n, n) in coordinate:
            return sec
        for next_c in next_coordinate(coordinate, new_b):
            if next_c not in visited:
                q.append((next_c, sec + 1))
                visited.append(next_c)

    return 0