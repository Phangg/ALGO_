import sys
from collections import deque

def bfs(s):
    q = deque()
    q.append(s)
    visited = [0] * 100001
    while q:
        s = q.popleft()
        for next in [s-1, s+1, s*2]:
            if 0 <= next <= 100000 and not visited[next]:
                if next == K:
                    return visited[s] + 1
                else:
                    q.append(next)
                    visited[next] = visited[s] + 1

N, K = map(int, sys.stdin.readline().split())
ans = 0
if N > K:
    while N != K:
        N -= 1
        ans += 1
elif N < K:
    ans = bfs(N)
print(ans)