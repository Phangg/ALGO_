import sys

n, d, k, c = map(int, sys.stdin.readline().split())
lst = list(int(sys.stdin.readline().rstrip()) for _ in range(n))

max_len = 0
for i in range(n):
    tmp = set()
    flag = 0
    for j in range(k):
        x = i + j
        if x >= n:
            x -= n
        tmp.add(lst[x])
        if lst[x] == c:
            flag = 1

    if max_len <= len(tmp):
        if flag:
            max_len = len(tmp)
        else:
            max_len = len(tmp)+1
print(max_len)