import sys
from collections import deque
from copy import deepcopy


def bfs(tmp_arr):
    q = deque()
    for i in range(n):
        for j in range(m):
            if tmp_arr[i][j] == 2:
                q.append((i, j))
    while q:
        x, y = q.popleft()
        for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nx, ny = x+dx, y+dy
            if (0 <= nx < n) and (0 <= ny < m) and tmp_arr[nx][ny] == 0:
                tmp_arr[nx][ny] = 2
                q.append((nx, ny))

    safety = 0
    for i in range(n):
        for j in range(m):
            if tmp_arr[i][j] == 0:
                safety += 1
    return safety


def make_wall(cnt):
    global answer
    if cnt == 3:
        tmp_arr = deepcopy(arr)
        answer = max(answer, bfs(tmp_arr))
        return

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j] = 1
                cnt += 1
                make_wall(cnt)
                cnt -= 1
                arr[i][j] = 0


n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


answer = 0
cnt = 0
make_wall(cnt)
print(answer)
