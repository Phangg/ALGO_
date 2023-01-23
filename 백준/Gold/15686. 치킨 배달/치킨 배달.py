import sys
from itertools import combinations
from collections import deque

# 0 : 빈칸 / 1 : 집 / 2 : 치킨집
# 크기가 n * n 인 도시
# 집의 개수 <= (2 * n)
# m <= 치킨집의 개수 <= 13
# (r1, c1)과 (r2, c2) 사이의 거리 -> |r1-r2| + |c1-c2|

n, m = map(int, sys.stdin.readline().split())

# 도시 정보 입력
city = []
for _ in range(n):
    city.append(list(map(int, sys.stdin.readline().split())))

h_cnt = 0
h_info = []
c_info = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            h_info.append((i, j))
            h_cnt += 1
        elif city[i][j] == 2:
            c_info.append((i, j))

min_ans = float('inf')

q = deque()
for case in combinations(c_info, m):
    for c in case:
        q.append(c)

    min_len = [float('inf')] * h_cnt
    while q:
        x, y = q.popleft()
        idx = 0
        for h1, h2 in h_info:
            tmp = abs(h1-x) + abs(h2-y)
            if tmp < min_len[idx]:
                min_len[idx] = tmp
            idx += 1
        total = sum(min_len)

        if total < min_ans:
            min_ans = total
            
print(min_ans)