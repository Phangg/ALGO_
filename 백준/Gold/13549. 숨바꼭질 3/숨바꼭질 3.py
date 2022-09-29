import sys
from collections import deque

def bfs(n):
    visited = [-1] * 100001
    q = deque()
    q.append(n)
    visited[n] = 0
    while q:
        s = q.popleft()
        for ns in [s-1, s+1, s*2]:
            if 0 <= ns < 100001 and visited[ns] == -1:
                if ns == (s*2):
                    visited[ns] = visited[s]
                    q.appendleft(ns)
                else:
                    visited[ns] = visited[s] + 1
                    q.append(ns)
            if ns == K:
                return visited[ns]

N, K = map(int, sys.stdin.readline().split())
if N < K:
    print(bfs(N))
else:
    print(N-K)