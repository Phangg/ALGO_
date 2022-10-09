import sys

N = int(sys.stdin.readline())
lst = [int(sys.stdin.readline()) for _ in range(N)]
dp = [0] * N

# 주어지는 포도잔의 수 (N)이 3보다 작을 경우마다 나누어서 출력
if N >= 4:
    dp[0] = lst[0]
    dp[1] = lst[0] + lst[1]
    dp[2] = max(dp[1], lst[0]+lst[2], lst[1]+lst[2])
    for i in range(3, N):
        dp[i] = max(dp[i-2]+lst[i], dp[i-3]+lst[i-1]+lst[i])
        if dp[i] < dp[i-1]:
            dp[i] = dp[i-1]
    print(max(dp[N-4:N]))
elif N == 3:
    print(max(lst[0] + lst[1], lst[0]+lst[2], lst[1]+lst[2]))
elif N == 2:
    print(lst[0]+lst[1])
else:
    print(lst[0])