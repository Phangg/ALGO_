import sys
from copy import deepcopy
from collections import deque
from itertools import combinations

def bfs(tmp_lst):
    while tmp_lst:
        i, j = tmp_lst.popleft()
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            while (0 <= ni < n) and (0 <= nj < n) and (arr[ni][nj] != 'O'):
                if arr[ni][nj] == 'S':
                    return True
                else:
                    ni += di
                    nj += dj
    return False

n = int(sys.stdin.readline())
arr = [list(sys.stdin.readline().split()) for _ in range(n)]

t_lst = deque()
o_lst = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'T':
            t_lst.append((i, j))
        elif arr[i][j] == 'X':
            o_lst.append((i, j))

comb_lst = list(combinations(o_lst, 3))
# print(comb_lst)

for coordinate in comb_lst:
    tmp_lst = deepcopy(t_lst)
    x1, y1 = coordinate[0]
    x2, y2 = coordinate[1]
    x3, y3 = coordinate[2]
    arr[x1][y1] = 'O'
    arr[x2][y2] = 'O'
    arr[x3][y3] = 'O'
    res = bfs(tmp_lst)
    if not res:
        print('YES')
        break
    arr[x1][y1] = 'X'
    arr[x2][y2] = 'X'
    arr[x3][y3] = 'X'
else:
    print('NO')