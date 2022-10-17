import sys
from collections import defaultdict

n, d, k, c = map(int, sys.stdin.readline().split())
lst = list(int(sys.stdin.readline().rstrip()) for _ in range(n))

eat = defaultdict(int)
cnt = 1
eat[c] = 1
for i in range(k):
    if eat[lst[i]] == 0:
        cnt += 1
    eat[lst[i]] += 1

answer = cnt
for left in range(n):
    right = (left+k) % n
    eat[lst[left]] -= 1
    if eat[lst[left]] == 0:
        cnt -= 1
    if eat[lst[right]] == 0:
        cnt += 1
    eat[lst[right]] += 1
    answer = max(answer, cnt)
print(answer)
