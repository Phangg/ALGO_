import sys

# n : 병사 인원
n = int(sys.stdin.readline())
# lst : 각 병사 전투력
lst = list(map(int, sys.stdin.readline().split()))

# dp : (큰 전투력부터 작은 전투력으로 정렬 된 상태) -> 조건 만족 + 최대 값이 되는 병사 인원 저장
dp = [1] * n

for i in range(n):
    for j in range(i):
        if lst[i] < lst[j]:
            dp[i] = max(dp[i], dp[j]+1)

# 전체 병사 - 최대 인원 
print(n - max(dp))