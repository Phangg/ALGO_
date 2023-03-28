import sys
from collections import deque
from itertools import combinations

def check_bfs(tmp_q, cnt):
    que = deque()
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    max_cnt = 0
    for t in tmp_q:
        que.append(t)
        visited[t[0]][t[1]] = 0
    while que:
        x, y = que.popleft()
        for xx, yy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nx, ny = x + xx, y + yy
            if (0 <= nx < n) and (0 <= ny < n) and (status[nx][ny] == 0) and (visited[nx][ny] == -1):
                que.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
                cnt -= 1
                max_cnt = max(max_cnt, visited[nx][ny])
                if cnt == 0:
                    return max_cnt

    if len(tmp_q) == cnt:
        return max_cnt
    return -1

# n * n 의 연구소
# m 개의 바이러스
# status : 연구소 상태
# 0은 빈 칸, 1은 벽, 2는 바이러스를 놓을 수 있는 칸
n, m = map(int, sys.stdin.readline().split())
status = []
virus_start = []
possible_cnt = 0
for p in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    status.append(row)
    for q in range(n):
        if row[q] == 2:
            virus_start.append((p, q))
            possible_cnt += 1
            row[q] = 0
        elif row[q] == 0:
            possible_cnt += 1

ans = []

com_lst = list(combinations(virus_start, m))
for com in com_lst:
    res = check_bfs(com, possible_cnt)
    if res != -1:
        ans.append(res)

if ans:
    print(min(ans))
else:
    print(-1)