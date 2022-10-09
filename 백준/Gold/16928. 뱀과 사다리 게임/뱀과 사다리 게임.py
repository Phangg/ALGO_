import sys
from collections import deque

def bfs(start):
    q = deque()
    q.append((start, 0))
    visited = [0] * 101
    visited[start] = 1
    while q:
        s, cnt = q.popleft()
        for next in range(1, 6+1):
            ns = s+next
            if 0 < ns <= 100:
                if not visited[ns]:
                    if type(board[ns]) == tuple:
                        visited[ns] = 1
                        q.append((board[ns][1], cnt+1))
                    else:
                        visited[ns] = 1
                        q.append((board[ns], cnt+1))
                    if ns == 100:
                        return q[-1][1]

board = [t for t in range(101)]
N, M = map(int, sys.stdin.readline().split())
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    board[x] = ('L', y)
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    board[u] = ('S', v)
print(bfs(board[1]))