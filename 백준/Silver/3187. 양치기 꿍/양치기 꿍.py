import sys
from collections import deque

# 일반적인 bfs
def bfs(i, j):
    global v, k
    q = deque()
    tmp_v, tmp_k = 0, 0
    visited[i][j] = 1
    q.append([i, j])
    while q:
        x, y = q.popleft()
        for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nx, ny = dx + x, dy + y
            if (0 <= nx < r) and (0 <= ny < c) and (arr[nx][ny] != '#') and (visited[nx][ny] == 0):
                q.append([nx, ny])
                visited[nx][ny] = 1
                if arr[nx][ny] == 'v':
                    tmp_v += 1
                elif arr[nx][ny] == 'k':
                    tmp_k += 1

    # 양과 늑대 중 어떤 개체가 살아남을지 체크
    if tmp_v >= tmp_k:
        v += tmp_v
    else:
        k += tmp_k


# r : 세로 / c : 가로
r, c = map(int, sys.stdin.readline().split())
# . : 빈공간 / # : 울타리 / v : 늑대 / k : 양
arr = [list(sys.stdin.readline().strip()) for _ in range(r)]
# visited : 방문 기록
visited = [[0] * c for _ in range(r)]

# v : 늑대 / k : 양
v, k = 0, 0

for i in range(r):
    for j in range(c):
        bfs(i, j)

print(k, v)