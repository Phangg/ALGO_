import sys
from collections import deque

# 총 F층으로 이루어진 고층 건물, 스타트링크의 위치는 G층, 지금 있는 곳은 S층, G층으로 이동하려고 함
# U버튼은 위로 U층을 가는 버튼, D버튼은 아래로 D층을 가는 버튼
f, s, g, u, d = map(int, sys.stdin.readline().split())

res = []
visited = [0] * (f + 1)
visited[s] = 1

if s == g:
    print(0)
    exit()

q = deque([(s, 0)])
while q:
    now, cnt = q.popleft()
    for move in [u, -d]:
        next = now + move
        if next == g:
            res.append(cnt + 1)
            break
        if (1 <= next <= f) and (visited[next] == 0):
            q.append((next, cnt + 1))
            visited[next] = 1
if res:
    print(min(res))
else:
    print("use the stairs")