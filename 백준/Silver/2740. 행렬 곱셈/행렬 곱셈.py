import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a_arr = [list(map(int, input().split())) for _ in range(n)]
m, k = map(int, input().split())
b_arr = [list(map(int, input().split())) for _ in range(m)]

res = [[0] * k for _ in range(n)]

for x in range(n):
    for y in range(k):
        for w in range(m):
            res[x][y] += (a_arr[x][w] * b_arr[w][y])

for i in range(n):
    for j in range(k):
        print(res[i][j], end=' ')
    print()