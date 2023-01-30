import sys
from collections import deque

def bfs(p, q):
    que = deque()
    que.append((p, q))
    visited[p][q] = 1

    while que:
        x, y = que.popleft()
        for xi, yj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nx, ny = x + xi, y + yj
            if nx == n:
                nx = 0
            if ny == m:
                ny = 0
            if nx == -1:
                nx = n - 1
            if ny == -1:
                ny = m - 1

            if donut[nx][ny] == 0 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                que.append((nx, ny))

    return 1


# n : 세로 , m : 가로
# donut : 도넛 2차원 그래프
n, m = map(int, sys.stdin.readline().split())
donut = []
for _ in range(n):
    donut.append(list(map(int, sys.stdin.readline().split())))

# ans : 탐험 가능 구역
# visited : 방문 구역 체크 용 2차원 배열
ans = 0
visited = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if (donut[i][j] == 0) and (visited[i][j] == 0):
            ans += bfs(i, j)

print(ans)