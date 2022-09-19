import sys

N, K = map(int, sys.stdin.readline().split())
coin_lst = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
coin_lst = coin_lst[::-1]

ans = 0
for coin in coin_lst:
    if (K // coin) > 0:
        ans += (K // coin)
        K = K % coin
print(ans)