import sys

n, m = map(int, sys.stdin.readline().split())
floor = [list(sys.stdin.readline().strip()) for _ in range(n)]

# 목재 개수
ans = 0

for i in range(n):
    for j in range(m):
        # '-' 일 때,
        if floor[i][j] == '-':
            # 마지막이 아니고, 다음 칸이 '-' 라면 continue
            if j + 1 != m and floor[i][j+1] == '-':
                continue
            # 마지막이거나 같은 목재가 아니라면 + 1
            else:
                ans += 1
        # '|' 일 때, (위와 같은 로직)
        else:
            if i + 1 != n and floor[i+1][j] == '|':
                continue
            else:
                ans += 1

print(ans)