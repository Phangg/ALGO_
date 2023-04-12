import sys
import heapq

def dij():
    q = []
    heapq.heappush(q, (cave[0][0], 0, 0))
    dist[0][0] = 0

    while q:
        cost, x, y = heapq.heappop(q)

        if (x == n-1) and (y == n-1):
            print(f'Problem {cnt}: {dist[x][y]}')
            break

        for ix, iy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nx, ny = x + ix, y + iy
            if (0 <= nx < n) and (0 <= ny < n):
                new_cost = cost + cave[nx][ny]
                if new_cost < dist[nx][ny]:
                    dist[nx][ny] = new_cost
                    heapq.heappush(q, (new_cost, nx, ny))


cnt = 1
while 1:
    n = int(sys.stdin.readline().strip())
    if n == 0:
        break
    cave = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    dist = [[float('inf')] * n for _ in range(n)]

    dij()
    cnt += 1