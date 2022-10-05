import sys
from collections import deque

def bfs(s):
    q = deque()
    visited = [0] * (N+1)
    q.append(s)
    visited[s] = 1
    while q:
        x = q.popleft()
        for next in cross_line[x]:
            if not visited[next]:
                q.append(next)
                visited[next] = visited[x] + 1
                if end in stop_station_line[next]:
                    return visited[next] - 1
    return float('inf')


N = int(sys.stdin.readline())
stop_station_line = [[] for _ in range(N+1)]
cross_line = [[] for _ in range(N+1)]
for n in range(1, N+1):
    tmp = list(map(int, sys.stdin.readline().split()))
    for x in range(1, len(tmp)):
        stop_station_line[n].append(tmp[x])
end = int(sys.stdin.readline())

for i in range(1, N+1):
    for j in range(len(stop_station_line[i])):
        for p in range(i+1, N+1):
            for q in range(len(stop_station_line[p])):
                if stop_station_line[i][j] == stop_station_line[p][q]:
                    cross_line[i].append(p)
                    cross_line[p].append(i)

min_v = float('inf')
flag = 0
for idx, lst in enumerate(stop_station_line):
    if 0 in lst:
        if end in lst:
            flag = 1
            break
        else:
            v = bfs(idx)
            if min_v > v:
                min_v = v
if flag:
    print(0)
elif min_v == float('inf'):
    print(-1)
else:
    print(min_v)