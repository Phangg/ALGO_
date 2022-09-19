import sys

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
res = []
tmp = 0
for n in lst:
    tmp += n
    res.append(tmp)
print(sum(res))