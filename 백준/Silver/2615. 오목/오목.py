import sys

def check(K):
    global res
    ans = []
    for i in range(N):
        for j in range(N):   # 우상    우     우하     하
            for di, dj in [[-1, 1], [0, 1], [1, 1], [1, 0]]:
                temp = ''
                for m in range(5):
                    ni, nj = i + di * m, j + dj * m
                    if (0 <= ni < N) and (0 <= nj < N) and (omok[ni][nj] == K):
                        temp += 't'
                    if temp == 't' * 5:
                        if (0 <= i - di < N) and (0 <= j - dj < N) and (omok[i - di][j - dj] == K):
                            break
                        if (0 <= ni + di < N) and (0 <= nj + dj < N) and (omok[ni + di][nj + dj] == K):
                            break
                        res = K
                        ans = [i + 1, j + 1]
                        break
    return ans

N = 19
omok = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

res = 0
a = check(1)
b = check(2)

print(res)
if a:
    print(*a)
elif b:
    print(*b)