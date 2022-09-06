import sys
from collections import deque

def bfs(arr, x, y):
    q = deque()
    q.append((x, y))
    arr[x][y] = 0
    cnt = 1

    while q:
        x, y = q.popleft()
        for dx, dy in [[0,1], [1,0], [0,-1], [-1,0]]:
            nx, ny = x+dx, y+dy
            if (0 <= nx < N) and (0 <= ny < N) and (lst[nx][ny] == 1):
                q.append((nx, ny))
                arr[nx][ny] = 0
                cnt += 1
    return cnt

N = int(sys.stdin.readline())
lst = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

ans = []
for i in range(N):
    for j in range(N):
        if lst[i][j] == 1:
            ans.append(bfs(lst, i, j))

ans.sort()
print(len(ans))
for a in ans:
    print(a)