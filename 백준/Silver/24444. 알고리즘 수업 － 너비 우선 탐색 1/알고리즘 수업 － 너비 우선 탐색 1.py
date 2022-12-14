import sys
from collections import deque

def bfs(s, lst):
    cnt = 1
    visited[s] = 1
    q = deque([s])
    while q:
        s = q.popleft()
        for i in lst[s]:
            if visited[i] == 0:
                cnt += 1
                visited[i] = cnt
                q.append(i)


N, M, R = map(int, sys.stdin.readline().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    arr[x].append(y)
    arr[y].append(x)

for j in arr:
    j.sort()

visited = [0] * (N+1)
bfs(R, arr)

for ans in visited[1:]:
    print(ans)