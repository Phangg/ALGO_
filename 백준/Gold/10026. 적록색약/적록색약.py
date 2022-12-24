import sys
from collections import deque

# bfs
def check(i, j):
    visited[i][j] = 1
    q = deque()
    q.append((i, j))

    while q:
        x, y = q.popleft()
        for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nx, ny = x+dx, y+dy
            # 범위 안에 있고, 현재와 다음이 같고, 방문한 적이 없을 경우
            if (0 <= nx < n) and (0 <= ny < n) and (color[x][y] == color[nx][ny]) and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = 1


# n : 구역의 개수
n = int(sys.stdin.readline())
# color : 구역
color = []
for _ in range(n):
    color.append(list(sys.stdin.readline().strip()))
# 방문 구역 표시용
visited = [[0 for _ in range(n)] for _ in range(n)]

# 적녹색약 X cnt
no_cnt = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            check(i, j)
            no_cnt += 1

# 방문 구역 표시용 재정의
visited = [[0 for _ in range(n)] for _ in range(n)]

# 적녹색약 cnt
cnt = 0
for i in range(n):
    for j in range(n):
        # R 과 G 를 G 로 통일
        if color[i][j] == 'R':
            color[i][j] = 'G'
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            check(i, j)
            cnt += 1

print(no_cnt, cnt)