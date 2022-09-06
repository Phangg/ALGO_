import sys
N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

ans = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if ans < nums[i]+nums[j]+nums[k] <= M:
                ans = nums[i]+nums[j]+nums[k]

print(ans)