import sys
from collections import deque

def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    cnt = 1
    while q:
        x, y = q.popleft()
        for xx, yy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nx, ny = x + xx, y + yy
            if (0 <= nx < n) and (0 <= ny < n) and (board[nx][ny] == 0) and (visited[nx][ny] == 0):
                q.append((nx, ny))
                visited[nx][ny] = 1
                cnt += 1
    return cnt


# n * n 의 board
# m 개의 버섯 포자 보유
# 버섯 포자는 심어진 칸을 포함해 최대 K 개의 연결된 (버섯이 자랄 수 있는) 칸에 버섯을 자라게 함
n, m, k = map(int, sys.stdin.readline().split())
board = []
zero_cnt = 0
for _ in range(n):
    lst = list(map(int, sys.stdin.readline().split()))
    zero_cnt += lst.count(0)
    board.append(lst)

if zero_cnt == 0:
    print('IMPOSSIBLE')
    exit()
    
elif k == 1:
    if zero_cnt <= m:
        print('POSSIBLE')
        print(m - zero_cnt)
    else:
        print('IMPOSSIBLE')
    exit()

visited = [[0 for _ in range(n)] for _ in range(n)]

ans = 0

for i in range(n):
    for j in range(n):
        if (board[i][j] == 0) and (visited[i][j] == 0):
            res = bfs(i, j)
            if res % k == 0:
                ans += (res // k)
            else:
                ans += ((res // k) + 1)
if (m - ans) >= 0:
    print('POSSIBLE')
    print(m - ans)
else:
    print('IMPOSSIBLE')