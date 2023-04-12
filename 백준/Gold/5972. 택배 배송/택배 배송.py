import sys
import heapq

def dij(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0
    
    while q:
        cur_dist, cur_node = heapq.heappop(q)
        if dist[cur_node] < cur_dist:
            continue
            
        for next_node, next_dist in lst[cur_node]:
            cost = cur_dist + next_dist
            if cost < dist[next_node]:
                dist[next_node] = cost
                heapq.heappush(q, (cost, next_node))


n, m = map(int, sys.stdin.readline().split())
lst = [[] for _ in range(n + 1)]
dist = [float('inf')] * (n + 1)
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    lst[a].append((b, c))
    lst[b].append((a, c))

dij(1)
print(dist[n])