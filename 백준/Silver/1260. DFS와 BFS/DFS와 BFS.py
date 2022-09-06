import sys
from collections import deque

def dfs(graph, v, visited):
    visited[v] = 1
    print(v, end=' ')
    for i in graph[v]:
        if visited[i] == 0:
            dfs(graph, i, visited)


def bfs(x, graph, visited):
    q = deque([x])
    visited[x] = 1
    while q:
        x = q.popleft()
        print(x, end=' ')
        for i in graph[x]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1


N, M, V = map(int, sys.stdin.readline().split())
graph = [[]*(N+1) for _ in range(N+1)]
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
for s, e in lst:
    graph[s].append(e)
    graph[e].append(s)
for r in range(1, N+1):
    graph[r].sort()

visited = [0] * (N+1)
dfs(graph, V, visited)
print()
visited = [0] * (N+1)
bfs(V, graph, visited)