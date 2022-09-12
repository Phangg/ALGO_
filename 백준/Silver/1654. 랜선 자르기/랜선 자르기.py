import sys
import math

K, N = map(int, sys.stdin.readline().split())
lan = [int(sys.stdin.readline()) for _ in range(K)]
lan.sort()
s = 1
e = lan[-1]

ans = 0
while s <= e:
    cnt = 0
    mid = math.ceil((s + e)/2)
    for ll in lan:
        cnt += (ll // mid)
    if cnt >= N:
        s = mid + 1
    elif cnt < N:
        e = mid - 1
print(e)
