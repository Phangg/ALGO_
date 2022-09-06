import sys

N, M = list(map(int, sys.stdin.readline().split()))

ans = 1
for _ in range(M):
    k = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    if nums != sorted(nums, reverse=True):
        ans = 0
        break

if ans == 1:
    print('Yes')
else:
    print('No')