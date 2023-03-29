import sys

# 가로 2 칸 , 세로 n 칸
n = int(sys.stdin.readline())

# 사자들이 살고 있는데 사자들을 우리에 가둘 때, 가로로도 세로로도 붙어 있게 배치할 수는 없다.
dp = [0 for _ in range(n + 1)]

# 사자를 한 마리도 배치하지 않는 경우도 하나의 경우의 수
dp[0] = 1
dp[1] = 3

for i in range(2, n+1):
    dp[i] = (dp[i-2] + (dp[i-1] * 2)) % 9901

print(dp[n])